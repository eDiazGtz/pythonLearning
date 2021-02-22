from django.shortcuts import render, redirect

# Create your views here.
def root(request):
    return render(request, "root.html")

def result(request):
    if(request.method == "POST"):
        request.session['firstName'] = request.POST["firstName"]
        request.session['lastName'] = request.POST["lastName"]
        request.session['dojo'] = request.POST["dojo"]
        request.session['language'] = request.POST["language"]
        request.session['comment'] = request.POST["comment"]
        return redirect('/result')
    return render(request, "result.html")