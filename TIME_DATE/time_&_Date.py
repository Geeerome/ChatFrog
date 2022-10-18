import time
from datetime import datetime
import pytz

#THIS UTILITY MODULE IS ONLY GETTING THE TIME THAT WAS SET IN LOCAL MACHINE

format = "%Y-%m-%d %H:%M:%S"

def DateAndTime_Now():
    timenow=datetime.now()
    timenow=timenow.strftime("%Y-%m-%d %H:%M:%S")	
    d1=datetime.strptime(timenow,"%Y-%m-%d %H:%M:%S")
    #returns date and time with this format 2022-10-18 10:03:48
    return d1

def epoch_to_dateTime(epx_data):
    entrytimein = datetime.fromtimestamp(int(epx_data))
    entrytimeins = str(entrytimein)
    return(entrytimeins)
    #returns date and time with this format 2022-10-18 10:03:48

def dateTime_to_epoch(timenow):
    epoch = int(time.mktime(time.strptime(timenow, format)))
    timeinEpoch = str(epoch)
    return timeinEpoch


def Time_Now():
    timenow=datetime.now()
    timenow=timenow.strftime("%H:%M:%S")
    #returns date and time with this format 10:03:48
    return timenow


########################### PYTZ METHOD

def parse_date_time(date_time):
    localize = pytz.utc.localize(date_time)
    parsed_datetime= localize.strftime("%Y-%m-%d %H:%M:%S")
    return parsed_datetime

def parse_date_only(date):
    str_date_to_obj = datetime.strptime(date, "%Y-%m-%d")
    return str_date_to_obj.strftime("%Y-%m-%d")





