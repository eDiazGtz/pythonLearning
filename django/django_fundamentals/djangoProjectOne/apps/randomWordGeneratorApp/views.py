from django.shortcuts import render
from django.utils.crypto import get_random_string

# Create your views here.
def landing(request):
    if('string' not in request.session):
        request.session['string'] = ""
    myString = get_random_string(length=14)
    print(myString)
    request.session['string'] = myString
    return render(request, "randomLanding.html")