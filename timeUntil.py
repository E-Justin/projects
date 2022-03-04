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
        self.hoursUnitl = 0
        self.minutesUntil = 0
        self.secondsUntil = 0

CountDown = Time()

now = datetime.now()
CountDown.currentTime = now.strftime("%m/%d/%Y, %H:%M:%S")
# gets date/time in this format: 03/04/2022, 08:47:57
#            index:              01234567890123456789


CountDown.nowHour = int(CountDown.currentTime[12:14]) # extracts hour from time/date
CountDown.nowMinute = int(CountDown.currentTime[15:17]) # extracts minute(s) from time/date
CountDown.nowSecond = int(CountDown.currentTime[18:]) # extracts second(s) from time/ date



# CountDown.futureTime = pyip.inputStr("Enter the time that you want to countdown to in standard time (hh:mm)")
CountDown.futureTime = "04:15"
# CountDown.futureAMPM = pyip.inputChoice(["AM", "PM"], "is that AM or PM?")
CountDown.futureAMPM = "PM"
CountDown.futureHour = int(CountDown.futureTime[0:2])
if CountDown.futureAMPM == "PM":
    CountDown.futureHour += 12
CountDown.futureMinute = int(CountDown.futureTime[3:5])

print(str(CountDown.futureHour) + ":" + str(CountDown.futureMinute))
print(str(CountDown.nowHour) + ":" + str(CountDown.nowMinute))




