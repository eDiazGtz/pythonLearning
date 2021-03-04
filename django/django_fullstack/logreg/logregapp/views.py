from django.shortcuts import render, redirect


# Create your views here.
def landing(request):
    return render(request, "landing.html")

def register(request):
    return redirect("/dashboard")

def dashboard(request):
    return render(request, "dashboard.html")