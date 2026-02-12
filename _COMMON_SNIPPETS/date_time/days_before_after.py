# get the time in days before and/or after current date

from datetime import date, timedelta

date_before = (date.today()-timedelta(days=30))
date_after = (date.today()+timedelta(days=30))

print(date_before)
print(date_after)