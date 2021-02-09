from django.shortcuts import render, redirect
import random

def home(request):
    return render(request, "landing.html")

def assign(request):
    #Do something with the form Data --- VIEWS IS CONTROLLER
    if(request.method == 'POST'):
#        print(request.POST['username']) #prints the valus of POST
        #store name in session
        request.session['username'] = request.POST['username']
        return redirect("/game")
    else:
        return render(request, "landing.html")

def game(request):
    return render(request, "game.html")

def processGame(request):
    #pass results to user
    #post request -- redirect
    if(request.method == 'POST'):
    #retrieve user value
        guess = request.POST['guess']
    #generate random value between 1-10
        randomNum = round(random.random() * 9 + 1)
        if(guess == randomNum):
            request.session['result'] = f"{request.session['username']} guessed the correct number: {guess}!"
        else:
            request.session['result'] = f"{request.session['username']} got it wrong! Try again."
        return redirect("/game")
    else:
        return redirect("/")