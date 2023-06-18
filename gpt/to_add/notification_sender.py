import time
import winsound


# Note: all these functions are not very useful, the final alarms will probably just be done in frontend

def set_alarm(hour, minute):
    while True:
        current_time = time.localtime()
        if current_time.tm_hour == hour and current_time.tm_min == minute:
            print("Alarm triggered!")
            winsound.Beep(1000, 1000) 
            break
        time.sleep(60)  


def set_timer(seconds):
    print(f"Timer set for {seconds} seconds.")
    time.sleep(seconds)
    print("Timer finished!")
    winsound.Beep(1000, 1000) 


def set_reminder(message, delay):
    print(f"Reminder set: {message}")
    time.sleep(delay)
    print("Reminder:", message)
    winsound.Beep(1000, 1000)  



