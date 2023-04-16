import datetime

sec = int(input('Please enter time in seconds: '))

# from datetime
time = str(datetime.timedelta(seconds=sec))

print(f'{time}')
