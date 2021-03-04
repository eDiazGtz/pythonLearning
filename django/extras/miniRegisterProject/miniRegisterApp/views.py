from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def landing(request):
    regform = RegisterForm()
    context = {
        "regForm":regform
    }
    return render(request, "landing.html", context)

# Inside your app's views.py file
# This is the method that is running in response to that form submission
def register(request):
    # Confirm that the HTTP verb was a POST
    if request.method == "POST":
        # Bind the POST data to an instance of our RegisterForm
        bound_form = RegisterForm(request.POST)
        # Now test that bound_form using built-in methods!
        # *************************
        print(bound_form.is_valid()) # True or False, based on the validations that were set!
        print(bound_form.errors) # Any errors in this form as a dictionary
        # *************************
    return redirect('/')

def dashboard(request):
    return render(request, "dashboard.html")
