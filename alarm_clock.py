

from datetime import datetime

user_time = input("Enter the time in this format (HH:MM:SS): ")

f = True
while f:
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    if current_time == user_time:
        f = False

print("Time's up")