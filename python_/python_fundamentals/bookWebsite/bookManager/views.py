from datetime import datetime
from django.shortcuts import render, redirect

HOURS_OF_OPERATION = [
    {'day': 'Monday', 'open': '7AM', 'close': '5PM'},
    {'day': 'Tuesday', 'open': '8AM', 'close': '6PM'},
    {'day': 'Wednesday', 'open': 'closed', 'close': 'closed'},
    {'day': 'Thursday', 'open': '9AM', 'close': '5PM'},
    {'day': 'Friday', 'open': '10AM', 'close': '4PM'},
    {'day': 'Saturday', 'open': '11AM', 'close': '3PM'},
    {'day': 'Sunday', 'open': 'closed', 'close': 'closed'},
]

# Create your views here.
def index(request):
    dayOfWeek = datetime.today().weekday() #returns a number 0-7; 0 = Monday; <- Teachers notes: probably means 0-6
    context = {
        'todaysHours':HOURS_OF_OPERATION[dayOfWeek],
        'hoursOfOperation': HOURS_OF_OPERATION
    }
    return render(request, 'index.html', context)

def addBook(request):
    if (request.method == 'POST'):
        #look for books dictionary in session; if dictionary doesn't exist create one
        if ('books' not in request.session):
            request.session['books'] = []
        #sets value for title and author -- the checks @NotBlank
        title = request.POST.get('title', None) #.get will search for the Key -- else will set it to 'None' (2nd Param)
        author = request.POST.get('author', None)
        #checking if NotBlank
        if (not title or not author):
            return redirect(request, '/addBook')

        #Save Book to DB
        request.session['books'].append({
            'id': len(request.session['books']),
            'title': title,
            'author': author
        })
        request.session.save()
        print(request.session['books'])
        return redirect('/book') #always redirect after POST
    else:
        return render(request, 'addBook.html')

def seeBook(request):
    return render(request, 'book.html')