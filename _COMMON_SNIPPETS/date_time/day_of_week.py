# methods to output the day of the week

# Method 1: Integer value where Monday is 0, Sunday is 6
from datetime import datetime

print(datetime.today().weekday())

# Method 2: Returns String of Day
from datetime import date
import calendar
curr_date = date.today()
print(calendar.day_name[curr_date.weekday()])


# Method 3: Uses Pandas timestamp
import pandas as pd

temp = pd.Timestamp('2023-07-30')
print(temp.dayofweek, temp.day_name())