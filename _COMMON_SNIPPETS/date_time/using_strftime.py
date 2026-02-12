from datetime import datetime

# sets variable with current  date and time
now = datetime.now()

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
time = now.strftime("%H:%M:%S")


# Legend
# -------------------------------------------------------
# %a     Sun
# %A     Sunday
# %b     Mar
# %B     March
# %m     03
# %y     25
# %Y     2025
# %H     20
# %I     08
# %M     06
# %S     05
# %c     Sun Sep 22 
# %x     09/22/24
# %X     20:08:05
# %p     AM