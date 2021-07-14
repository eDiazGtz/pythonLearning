from django.shortcuts import render, redirect
import random, collections
from datetime import datetime
from pytz import timezone
import pytz

# Create your views here.
def root(request):
    if('gold' not in request.session):
        request.session['gold'] = 0
    if('activities' not in request.session):
        request.session['activities'] = []
    return render(request, "root.html")

def findgold(request):

    if(request.method == 'POST'):
        location = request.POST['building']
        userGold = request.session['gold']
        activities = request.session['activities']

        date_format='%m/%d/%Y %H:%M:%S %Z'
        date = datetime.now(tz=pytz.utc)
        date = date.astimezone(timezone('US/Pacific'))
        myTime = date.strftime(date_format)

        if(location == 'farm'):
            thisTurnGold = round(random.random() * 10 + 10)
            myString = "You entered a Farm and earned " + str(thisTurnGold) + " Gold. " + myTime

        elif(location == 'cave'):
            thisTurnGold = round(random.random() * 5 + 5)
            myString = "You entered a Cave and earned " + str(thisTurnGold) + " Gold. " + myTime

        elif(location == 'house'):
            thisTurnGold = round(random.random() * 3 + 2)
            myString = "You entered a House and earned " + str(thisTurnGold) + " Gold. " + myTime

        elif(location == 'casino'):
            thisTurnGold = round(random.random() * 50)
            gainOrLoss = round(random.random() + 1)
            #Gain: 1 means loss of $$. 2 means Gain of $$
            if(gainOrLoss == 1):
                myString = "You entered a Casino and lost " + str(thisTurnGold) + " Gold. " + myTime
            else:
                myString = "You entered a Casino and won " + str(thisTurnGold) + " Gold! " + myTime

        userGold += thisTurnGold
        request.session['gold'] = userGold
        print(myString)
        request.session['activities'].insert(0, myString)
        # request.session['activities'] = activities

        return redirect("/")

    return redirect("/")

def reset(request):
    request.session.flush()
    return redirect("/")
