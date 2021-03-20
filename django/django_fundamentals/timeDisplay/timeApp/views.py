from django.shortcuts import render
# from time import gmtime, strftime
from datetime import datetime
from pytz import timezone
import pytz

# # Create your views here.
# def root(request):
#     context = {
#         "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
#     }
#     return render(request,'root.html', context)

def root(request):
    #date format
    date_format='%m/%d/%Y %H:%M:%S %Z'
    #setting time to now and TimeZone to UTC
    date = date.astimezone(timezonte = datetime.now(tz=pytz.utc))
    #setting TZ to US PACIFIC('US/Pacific'))
    date = date.astimezone(timezone('US/Pacific'))
    # displaying time
    myTime = date.strftime(date_format)
    context = {
        "time": myTime
    }
    return render(request, "root.html", context)