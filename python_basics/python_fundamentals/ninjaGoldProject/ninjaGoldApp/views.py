from django.shortcuts import render, redirect
from datetime import datetime
from pytz import timezone
import random, pytz

# Create your views here.
def landing(request):
    if('gold' not in request.session):
        request.session['gold'] = 0
    if('activities' not in request.session):
        request.session['activities'] = []
    return render(request, "landing.html")

def processMoney(request):
    if(request.method == 'POST'):
        location = request.POST['location']
        userGold = request.session['gold']
        activities = request.session['activities']

        date_format='%m/%d/%Y %H:%M:%S %Z'
        date = datetime.now(tz=pytz.utc)
        date = date.astimezone(timezone('US/Pacific'))
        myTime = date.strftime(date_format)

        if(location == 'farm'):
            #add 10-20 gold
            thisTurnGold = round(random.random() * 10 + 10)
            thisTurnString = f"You walk into a {location} and work hard! Gain {thisTurnGold} Gold! Hooray! {myTime}"
        elif(location == 'cave'):
            #5-10 House gold
            thisTurnGold = round(random.random() * 5 + 5)
            thisTurnString = f"You walk into a {location} and investigate! Located {thisTurnGold} Gold! Nice! {myTime}"
        elif(location == 'house'):
            #2-5 House gold
            thisTurnGold = round(random.random() * 3 + 2)
            thisTurnString = f"You walk into a {location} and clean up! Found {thisTurnGold} Gold! I love couches! {myTime}"
        else:
            takesOrGains = round(random.random() + 1)
            if(takesOrGains == 1):
                thisTurnGold = round(random.random() * 50)
                thisTurnString = f"You walk into a {location} and gamble! Lose {thisTurnGold} Gold! Oh-No!! {myTime}"
                activities.insert(0, thisTurnString)
                request.session['activities'] = activities
                request.session['gold'] = userGold - thisTurnGold
                return redirect("/")  

            else:
                thisTurnGold = round(random.random() * 50)
                thisTurnString = f"You walk into a {location} and gamble! Win {thisTurnGold} Gold! Hooray! {myTime}"



        activities.insert(0, thisTurnString)
        request.session['activities'] = activities
        request.session['gold'] = userGold + thisTurnGold
    return redirect("/")
