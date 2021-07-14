from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, RawRegistrationForm
from .models import User
import bcrypt

# Create your views here.
def landing(request):
    regForm = RegistrationForm()
    context = {
        "regForm":regForm
    }
    return render(request, "logReg.html", context)


def register(request):
    if(request.method == "POST"):
        regForm = RegistrationForm(request.POST) #back-end re-validating in case front-end fails
        
        if regForm.is_valid(): #Uses django built-in validations
            user = regForm.save()
            #log in
            return redirect('/dashboard')
        else:
            context = {
                'reg_form':RegistrationForm(request.POST)
            }
            return render(request, "logReg.html", context)
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
    return render(request, "dashboard.html")

def logout(request):
    request.session.flush()
    return redirect('/')