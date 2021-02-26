from django.shortcuts import render, redirect
from .models import User, Ninja, Dojo

# Create your views here.
def landing(request):
    if(request.method == 'POST'):
        newUser = User.objects.create(firstName=request.POST['firstName'],lastName=request.POST['lastName'],emailAddress=request.POST['emailAddress'],age=request.POST['age'])
        newUser.save()
        return redirect("/dojo")
    context = {
        'users':User.objects.all()
    }
    return render(request,"dashboard.html", context)

def dojo(request):
    if(request.method == 'POST'):
        formInput = request.POST['formInput']
        if(formInput == "dojo"):
            newDojo = Dojo.objects.create(name=request.POST['name'],city=request.POST['city'],state=request.POST['state'])
            newDojo.save()
            return redirect("/dojo")
        elif(formInput == "ninja"):
            thisDojo = Dojo.objects.get(id=request.POST['dojoLocation'])
            newNinja = Ninja.objects.create(firstName=request.POST['firstName'],lastName=request.POST['lastName'],dojo=thisDojo)
            newNinja.save()
            return redirect("/dojo")
    context = {
        "dojos":Dojo.objects.all()
    }
    return render(request, "dojo.html", context)
