from django.shortcuts import render

# Create your views here.
def validations(request, postData):
    date = postData["birthday"]
    strfdate(date) #mm-yyyy
    .split('-', str)
    list = ["11", '1990']
    year = int(list[1]) + 13

    datimg("2002", 3, 6)

    
    return render(request, "index.html")