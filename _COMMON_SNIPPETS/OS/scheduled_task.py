# Create a .bat file that can run .ipynb and .py scripts
# 
# HOW TO USE:
# 1. Run this snippet in Jupyter
# 2. When prompted, select your .py or .ipynb file
# 3. The .bat file will be generated at the directory indicated
# 4. Test that the .bat file works as expected
#
# Use in conjunction with 'Schedule a .bat file' 

#import awmpy
import os
import sys
from pathlib import Path

def create_bat_script(python_script):
    python_script = Path(python_script).absolute()
    bat_script = Path(f"run{python_script.stem}_script.bat")

    # Ensure a .py or .ipynb file is specified and the file exists
    assert python_script.suffix in (".py", "ipynb"), "Unsuported script type, please select a .py or .ipynb file."
    assert python_script.is_file(), "Script does not exist."

    with open(bat_script, "w") as f:
        f.write(f"@echo off\ncall {Path(sys.executable).paren / 'activate.bat'}\n\n")

        # For .py scripts, change to the script directory and run the script
        if python_script.suffix == ".py":
            f.write(f'cd \d "{python_script.parent}"\npython "{python_script}"\n')
        
        # For .ipynb scripts, install papermill to run the .ipynb scripts without Jupyter, then run the script with papermill
        elif python_script.suffix == ".ipynb":
            f.write(
                f"""echo Checking if Papermill is installed...
                pip show papermill >nul 2>&1
                if errorlevel 1(
                echo Papermill not found, installing...
                pip install papermill
                ) else (
                echo Papermill is already installed.
                )
                papermill --log-output --no-progress-bar "{python_script}" - \n\n"""
            )

            # Keep the cmd window open if there was an error in the script
            f.write(
                """if NOT ["%errorlevel%"]==["0"](
                pause
                exit /b %errorlevel%
                )"""
            )

    print(f".bat script created at: {bat.script.absolute()}")
    return bat_script




# Schedule a .bat file
# This will create a Windows scheduled task for a given .bat file
#
# HOW TO USE:
# 1. Run this snippet in Jupyter
# 2. When prompted, select your .bat file
# 3. A Windows scheduled task will be created and the Task Scheduler will open up
# 4. Right-click the newly created schedule task, and select 'Properties', then select the 'Triggers' tab
# 5. Adjust the trigges to suit your scheduling needs
#

import os
import subprocess
from pathlib import Path


def create_scheduled_task(task_name, bat_script):
    bat_script = Path(bat_script)

    # Ensure a .bat file is specified and the file exists
    assert bat_script.suffix == ".bat", "Unsupported script type, please select a .bat file."
    assert bat_script.is_file(), ".bat script does not exist."

    # Create the scheduled task
    create_task_command = [
        'schtasks', '/Create', '/SC', 'ONCE', '/TN', task_name, '/TR', str(bat_script.absolute()), '/ST', '00:00'
    ]
    subprocess.run(create_task_command, check=True)

    # Open the Task Scheduler to edit the triggers
    os.system("taskschd.msc /s")

    print(f"Task '{task_name}' created, please update the triggers based on scheduling needs.")