import time
from win10toast import ToastNotifier
import datetime

def get_time_input():
    hour = int(input("Hrs. :"))
    minutes = int(input("Min. :"))
    seconds = int(input("Sec. :"))
    time_interval = seconds + (minutes * 60) + (hour * 3600)
    return time_interval

def log():
    now = datetime.datetime.now()
    start_time = now.strftime("%H:%M:%S")

    with open("log.txt", 'a') as file:
        file.write(f"You drank water at {now} \n")
    return 0

def notify():
    notification = ToastNotifier()
    notification.show_toast("Time to drink water")
    log()
    return 0

def starttime(time_interval):
    while True:
        time.sleep(time_interval)
        notify()

if __name__ == '__main__':
    time_interval = get_time_input()
    starttime(time_interval)