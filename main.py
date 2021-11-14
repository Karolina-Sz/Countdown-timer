import datetime
import time

while True:
    try:
        print("Hello. This is a countdown timer.")
        my_string = str(input('Enter date and time to which you want to countdown in this exact format (yyyy-mm-dd hh:mm): '))
        time_alarm = datetime.datetime.strptime(my_string, "%Y-%m-%d %H:%M")

        def chop_microseconds(time_delta):
            return time_delta - datetime.timedelta(microseconds=time_delta.microseconds)

        while True:
            time_now = datetime.datetime.now()
            time_delta = (time_alarm - time_now)
            time_delta_rounded = chop_microseconds(time_delta)
            if time_alarm > time_now:
                print(time_delta_rounded)
                time.sleep(1)
            else:
                print("Incorrect input.")


    except ValueError:
        print('ValueError: please put date and time in correct format')