""" This program will:
* ask the user to put in a time
* return how long until the input time """


from datetime import datetime
import pyinputplus as pyip

class Time:
    def __init__(self):
        self.futureTime = None
        self.futureAMPM = None
        self.currentTime = None
        self.nowHour = 0
        self.nowMinute = 0
        self.nowSecond = 0
        self.nowAMPM = None
        self.futureHour = 0
        self.futureMinute = 0
        self.futureSecond = 0
        self.hoursUntil = 0
        self.minutesUntil = 0
        self.secondsUntil = 0

#instantiate a class object
CountDown = Time()

# get the current time
now = datetime.now()
CountDown.currentTime = now.strftime("%m/%d/%Y, %H:%M:%S")
# gets date/time in this format: 03/04/2022, 08:47:57
#            index:              01234567890123456789


#get time and assign it to appropriate variable
CountDown.nowHour = int(CountDown.currentTime[12:14]) # extracts hour from time/date
CountDown.nowMinute = int(CountDown.currentTime[15:17]) # extracts minute(s) from time/date
CountDown.nowSecond = int(CountDown.currentTime[18:]) # extracts second(s) from time/ date


# get user to enter in the time they want to count down to
CountDown.futureTime = pyip.inputStr("Enter the time that you want to countdown to in standard time (hh:mm)")
#! CountDown.futureTime = "04:15"   #for testing purposes
CountDown.futureAMPM = pyip.inputChoice(["AM", "PM"], "is that AM or PM?")
#! CountDown.futureAMPM = "PM"      #for testing purposes

# assign time to appropriate variable
CountDown.futureHour = int(CountDown.futureTime[0:2])
if CountDown.futureAMPM == "PM":
    CountDown.futureHour += 12 # convert to military time to make calculations easier
CountDown.futureMinute = int(CountDown.futureTime[3:5])


# Calculate how long until the entered time
CountDown.secondsUntil = (60 - CountDown.nowSecond)

if CountDown.futureMinute > CountDown.nowMinute:
    CountDown.minutesUntil = CountDown.futureMinute - CountDown.nowMinute
    
else:
    CountDown.minutesUntil = ((60 - CountDown.nowMinute) + CountDown.futureMinute)
    CountDown.hoursUntil -= 1

CountDown.hoursUntil += (CountDown.futureHour - CountDown.nowHour)


# display how long until
print("~~~~~~~ Time Until ~~~~~~~")
print("Hours    " + str(CountDown.hoursUntil))
print("Minutes  " + str(CountDown.minutesUntil))
print("Seconds  " + str(CountDown.secondsUntil))




