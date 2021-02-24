from django.shortcuts import render, redirect
import random

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
        activities = request.session['activities']        
        userGold = request.session['gold']

        if(location == 'farm'):
            thisTurnGold = round(random.random() * 10 + 10)
            userGold += thisTurnGold
            request.session['gold'] = userGold
            myString = "You entered a Farm and earned " + str(thisTurnGold) + " Gold."
            activities.append(myString)
            request.session['activities'] = activities
            return redirect("/")

        if(location == 'cave'):
            thisTurnGold = round(random.random() * 5 + 5)
            userGold += thisTurnGold
            request.session['gold'] = userGold
            myString = "You entered a Cave and earned " + str(thisTurnGold) + " Gold."
            activities.append(myString)
            request.session['activities'] = activities
            return redirect("/")

        if(location == 'house'):
            thisTurnGold = round(random.random() * 3 + 2)
            userGold += thisTurnGold
            request.session['gold'] = userGold
            myString = "You entered a House and earned " + str(thisTurnGold) + " Gold."
            activities.append(myString)
            request.session['activities'] = activities
            return redirect("/")

        if(location == 'casino'):
            thisTurnGold = round(random.random() * 50)
            gainOrLoss = round(random.random() + 1)
            #Gain: 1 means loss of $$. 2 means Gain of $$
            if(gainOrLoss == 1):
                userGold -= thisTurnGold
                request.session['gold'] = userGold
                myString = "You entered a Casino and lost " + str(thisTurnGold) + " Gold."
                activities.append(myString)
                request.session['activities'] = activities
            else:
                userGold += thisTurnGold
                request.session['gold'] = userGold
                myString = "You entered a Casino and won " + str(thisTurnGold) + " Gold!"
                activities.append(myString)
                request.session['activities'] = activities
            return redirect("/")

    return redirect("/")