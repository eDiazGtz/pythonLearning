from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TvShow
from datetime import datetime

# landing
def landing(request):
    shows = TvShow.objects.all()
    context = {
        "shows":shows
    }
    return render(request, "dashboard.html", context)

# new
def new(request):
    return render(request, "new.html")

# createShow POST
def createShow(request):
    if request.method == 'POST':
        errors = TvShow.objects.createValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/shows/new')
        #add show to DB
        newShow = TvShow.objects.create(title=request.POST['title'], network=request.POST['network'], releaseDate=request.POST['releaseDate'], description=request.POST['description'])
        newShow.save()
        return redirect(f"/shows/{newShow.id}")
    return redirect("/")

# showShow
def showShow(request, show_id):
    thisShow = TvShow.objects.get(id=show_id)
    context = {
        "show":thisShow
    }    
    return render(request, "show.html", context)

# editShow
def editShow(request, show_id):
    thisShow = TvShow.objects.get(id=show_id)
    date = thisShow.releaseDate
    date_format='%Y-%m-%d'
    myDate = date.strftime(date_format)
    context = {
        "show":thisShow,
        "myDate":myDate,
    }
    return render(request, "edit.html", context)

# updateShow POST
def updateShow(request, show_id):
        #NEEDS GET REDIRECT
    if request.method == 'POST':
        errors = TvShow.objects.createValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect(f"/shows/{show_id}/edit")
        thisShow = TvShow.objects.get(id=show_id)
        thisShow.title = request.POST['title']
        thisShow.network = request.POST['network']
        thisShow.releaseDate = request.POST['releaseDate']
        thisShow.description = request.POST['description']
        thisShow.save()
    return redirect(f"/shows/{show_id}")

# deleteShow POST
def deleteShow(request, show_id):
        #NEEDS GET REDIRECT
    if request.method == 'POST':
        #Delete Show from DB
        thisShow = TvShow.objects.get(id=show_id)
        thisShow.delete()
    return redirect("/")
