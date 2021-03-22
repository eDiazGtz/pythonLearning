from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt


# Create your views here.
def landing(request):
    return render(request, "landing.html")

def register(request):
    if(request.method == "POST"):
        errors = User.objects.createValidator(request.POST)
        if(len(errors) > 0):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            hashpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            newUser = User.objects.create(firstName=request.POST['firstName'],lastName=request.POST['lastName'],email=request.POST['email'],password=hashpw)
            request.session['userId'] = newUser.id
            return redirect('/dashboard')
    return redirect('/')

def login(request):
    if(request.method == "POST"):
        user = User.objects.filter(email=request.POST['email'])
        if(len(user) > 0):
            user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['userId'] = user.id
                return redirect('/dashboard')
    messages.error(request, "Invalid Login Credentials.")
    return redirect('/')

def dashboard(request):
    if('userId' not in request.session):
        messages.error(request, "Oops! Login Required to be here! Please log in or Register.")
        return redirect('/')
    user = User.objects.get(id=request.session['userId'])
    context = {
        "user":user
    }
    return render(request, "dashboard.html", context)

def logout(request):
    request.session.flush()
    return redirect('/')