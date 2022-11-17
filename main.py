""" XXXXXXXX  CENTADAY BOT !!!   by Avery   XXXXXXXX

HERE are some notes and comments : 
UmU

OwO

UwU

seconds in a day: 86400
a centaday is a day divided by 100 
86400 seconds divided by 100 is 864.0 seconds

HH MM SS of 

"""
print("hello!")

secondsInCentaday=86400/100

print("there are", secondsInCentaday, "seconds in a centaday!")

import time


"""https://docs.python.org/3/library/time.html"""
# asctime means :
"""time.asctime([t])
Convert a tuple or struct_time representing a time as returned by gmtime() 
or localtime() to a string of the following form: 'Sun Jun 20 23:21:05 1993'. 
The day field is two characters long and is space padded if the day is a single 
digit, e.g.: 'Wed Jun  9 04:26:40 1993'.

If t is not provided, the current time as returned by localtime() is used. 
Locale information is not used by asctime()."""

#  \/ \/ \/ \/  here's tha code OwO   \/ \/ \/ \/

print("the local time is", time.asctime())

#  /\ /\ /\ /\ AMAZing. decaday!!!!   /\ /\ /\ /\

"""char 12, 13 is HH, char 15,16=MM    char 18,19=SS"""

def getSeconds():
    hourSeconds=20
    minuteSeconds=10
    secondSeconds=4
    secondsElapsed=hourSeconds+minuteSeconds+secondSeconds
    print("there have been",secondsElapsed,"seconds today!")


from datetime import datetime

current_dateTime = datetime.now()
clockHours=current_dateTime.hour
clockminutes=current_dateTime.minute
clockSeconds=current_dateTime.second

hoursToSec=clockHours*3600
minutesToSec=clockminutes*60

totalSecondsToday=hoursToSec+minutesToSec+clockSeconds
print("so far today there have been",totalSecondsToday,"seconds!")

percentOfDay=totalSecondsToday/secondsInCentaday
print("today is",percentOfDay,"percent over")

currentCentaday=int(percentOfDay)
print("the current centaday is",currentCentaday)

#  \/ \/ \/ \/     \/ \/ \/ \/
#  /\ /\ /\ /\     /\ /\ /\ /\