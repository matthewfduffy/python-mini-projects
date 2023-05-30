import datetime as dt

current_date = dt.date.today().strftime('%Y-%m-%d')
current_date_lst = current_date.split('-')

name = input('What is your name?: ')
b_date = input("Enter your birthday in yyyy-mm-dd format: ")

# days_until_b_date = current_date - int(b_date)

b_date_lst = b_date.split('-')

print(current_date_lst)
print(b_date_lst)

age = int(current_date_lst[0]) - int(b_date_lst[0])

print(age)
ordinal_suffix = {
    1: 'st',
    2: 'nd',
    3: 'rd',
    11: 'th',
    12: 'th',
    13: 'th'
    }

if current_date_lst[1] == b_date_lst[1] and current_date_lst[2] == b_date_lst[2]:
    print(f"{name} Today is your birthday! You are {age} years old.")

# TODO fix this to return days between today and user's birthday
else:
    age += 1
    b_date = dt.strftime(b_date, "%Y-%m-%d")
    delta = current_date.date() - b_date.date()
    print(delta)
    ordinal_suffix = ordinal_suffix.get((age +1) % 10 if not 10 < age <= 13 else age % 14, 'th')
    print(f"{name}, you still have x days until your {age}{ordinal_suffix} Birthday.")

