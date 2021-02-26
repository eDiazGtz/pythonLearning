from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def landing(request):
    if(request.method == 'POST'):
        newUser = User.objects.create(firstName=request.POST['firstName'],lastName=request.POST['lastName'],emailAddress=request.POST['emailAddress'],age=request.POST['age'])
        newUser.save()
        return redirect("/")
    context = {
        'users':User.objects.all()
    }
    return render(request,"dashboard.html", context)
