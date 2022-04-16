# import the time module
import time
from datetime import datetime

# define the countdown func.
def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	
	print(f'end {datetime.now()}')


# input time in seconds
t = input("Enter the time in seconds: ")
print(f'start {datetime.now()}')

# function call
countdown(int(t))
