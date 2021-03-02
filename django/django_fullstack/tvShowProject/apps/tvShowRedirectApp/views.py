from django.shortcuts import redirect

# Create your views here.
def redirectLanding(request):
    return redirect("/shows")