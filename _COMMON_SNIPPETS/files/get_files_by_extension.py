# Pass folder path while calling get_all_files()

import os

def get_all_files(folder):
    files = []

    for file in os.listdir(folder):
        # change parameter with file extension
        if file.endswith(".txt"):
            path = os.path.join(folder, file)
            files.append(path)
    
    return files


get_all_files(<folder_path>)