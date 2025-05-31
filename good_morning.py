# WAP capable of greeting you with good morning , good afternoon and good evening .
#  Your question should use module to get the current hour.

import time
t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
print(hour)

if (hour>=0 and hour<12):
    print("good morning sir!!")
elif(hour>=12 and hour<=17):
    print("good afternoon sir!!")
    if(hour>=17 and hour<0):
        print("good night sir!!")