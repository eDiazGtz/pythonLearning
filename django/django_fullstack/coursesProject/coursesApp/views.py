from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course
from datetime import datetime


# Create your views here.
def dashboard(request):
    courses = Course.objects.all()
    context = {
        "courses":courses
    }
    return render(request, "dashboard.html", context)

def add(request):
    if request.method == 'POST':
        errors = Course.objects.validations(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        newCourse = Course.objects.create(name=request.POST['name'], description=request.POST['description'])
        newCourse.save()
        messages.success(request, "New Course Added! You're awesome :)")
    return redirect("/")

def deletePage(request):
    if request.method == 'POST':
        print(request.POST)
        courseId = request.POST['id'] 
        course = Course.objects.get(id=courseId)
    context = {
        'course' : course
    }
    return render(request, "delete.html", context)

def destroy(request, courseId):
    if request.method == 'POST':
        
        thisCourse = Course.objects.get(id=courseId)
        thisCourse.delete()
    return redirect("/")
