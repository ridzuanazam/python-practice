# import time module

import time

my_time = int(input("Enter the time in seconds : "))

# use -1 step to reversed or use reversed()
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")