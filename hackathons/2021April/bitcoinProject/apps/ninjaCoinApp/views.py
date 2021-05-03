from django.shortcuts import render
from logregapp.models import *

# Create your views here.
def index(request):
        context = {
            "ninja":User.objects.get(session.)
        }
    return render(request, "ninja.html")
    