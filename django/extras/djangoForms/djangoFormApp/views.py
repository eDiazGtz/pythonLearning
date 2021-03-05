from django.shortcuts import render
from .forms import RegistrationForm, RegisterForm

# Create your views here.
def landing(request):
    regForm = RegisterForm()
    context = {
        "regForm":regForm
    }
    return render(request, "logreg.html", context)



def logout(request):
    request.session.flush()
    return redirect('/')