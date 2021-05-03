from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Dragon
from django.contrib.auth.forms import UserCreationForm #Built in User Creation Form 
from django.contrib.auth.forms import AuthenticationForm #Build in User Login Form
#So we can login User
from django.contrib.auth import login
from .forms import dragonForm, RegistrationForm
import bcrypt
from django.contrib.auth.decorators import login_required


# Create your views here.
def landing(request):
    #added context to pass Registration Form and later Login Form
    context = {
        'reg_form':RegistrationForm,
        'log_form':AuthenticationForm,
    }
    return render(request, "landing.html", context)

def register(request):
    if(request.method == "POST"):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #log user in
            login(request, user)
            return redirect('/dashboard')
        else:
            #Passing context to have form prefilled
            context = {
            'reg_form':form #changed value to form to carry values back
        }
            return render(request, "landing.html", context)
    return redirect('/')

def do_login(request): #there is going to be a method called login coming from Django so we will change name of method (CHANGE IN URLS.PY)
    if(request.method == "POST"):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            new_user = form.get_user() #Auth Forms have this getUser method which returns the new user that was just created/entered. 
            login(request, new_user) #to login we just need to pass request and the new_user
            return redirect('/dashboard')
        else:
            #Passing context to have form prefilled
            context = {
            'reg_form':UserCreationForm, 
            'log_form':form, #changed value to form to carry values back
        }
            return render(request, "landing.html", context)
    return redirect('/')

@login_required
def dashboard(request):
    #pushes us out -- because we're not creating userId in request.session --- we are being saved in session in a different way
    # if('userId' not in request.session):
    #     messages.error(request, "Oops! Login Required to be here! Please log in or Register.")
    #     return redirect('/')
    user = request.user #change everything to request -- as it now has access to the user (who is logged in)
    allDragons = Dragon.objects.all()
    context = {
        "user":user,
        "dragonForm":dragonForm,
        "allDragons":allDragons,
    }
    return render(request, "dashboard.html", context)

def logout(request):
    request.session.flush()
    return redirect('/')

def createDragon(request):
    if request.method == 'POST':
        user = request.user
        postedDragonForm = dragonForm(request.POST)
        if postedDragonForm.is_valid():
            #create new form
            newDragon = postedDragonForm.save(commit=False)
            newDragon.rider = user #user is now accesible from the request object so our rider is now request.user
            postedDragonForm.save()
            return redirect('/dashboard')
        else:
            context = {
                "user":user,
                "dragonForm":postedDragonForm,
            }
            return render(request, 'dashboard.html', context)
    return redirect('/dashboard')
