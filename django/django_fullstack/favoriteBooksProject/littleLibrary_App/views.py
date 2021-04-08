from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book
import bcrypt


# Create your views here.
def landing(request):
    return render(request, "landing.html")

def register(request):
    if(request.method == "POST"):
        errors = User.objects.createValidator(request.POST)
        if(len(errors) > 0):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            hashpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            newUser = User.objects.create(firstName=request.POST['firstName'],lastName=request.POST['lastName'],email=request.POST['email'],password=hashpw)
            request.session['userId'] = newUser.id
            return redirect('/dashboard')
    return redirect('/')

def login(request):
    if(request.method == "POST"):
        user = User.objects.filter(email=request.POST['email'])
        if(len(user) > 0):
            user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['userId'] = user.id
                return redirect('/dashboard')
    messages.error(request, "Invalid Login Credentials.")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

# --------------- DASHBOARD AND WEBSITE METHODS ----------------- #

def dashboard(request):
    if('userId' not in request.session):
        messages.error(request, "Oops! Login Required to be here! Please log in or Register.")
        return redirect('/')
    user = User.objects.get(id=request.session['userId'])
    allBooks = Book.objects.all()
    context = {
        "user":user,
        "allBooks":allBooks,
    }
    return render(request, "dashboard.html", context)

def newBook(request):
    if request.method == 'POST':
        errors = Book.objects.createValidator(request.POST)
        if(len(errors) > 0):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/dashboard')
        else:
            uploadedBy = User.objects.get(id=request.POST['uploadedBy'])
            newBook = Book.objects.create(title=request.POST['title'], description=request.POST['description'], uploadedBy=uploadedBy)
            newBook.usersWhoFavorite.add(uploadedBy)
    return redirect('/dashboard')

def showBook(request, bookId):
    if('userId' not in request.session):
        messages.error(request, "Oops! Login Required to be here! Please log in or Register.")
        return redirect('/')
    user = User.objects.get(id=request.session['userId'])
    thisBook = Book.objects.get(id=bookId)
    context = {
        "user":user,
        "book":thisBook,
    }
    return render(request, "show.html", context)

def updateBook(request, bookId):
    if('userId' not in request.session):
        messages.error(request, "Oops! Login Required to be here! Please log in or Register.")
        return redirect('/')
    if request.method == 'POST':
        errors = Book.objects.createValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/{bookId}/show")
        else:
            thisBook = Book.objects.get(id=bookId)
            user = User.objects.get(id=request.session['userId'])
            if user.id == thisBook.uploadedBy.id:
                thisBook.title = request.POST['title']
                thisBook.description = request.POST['description']
                thisBook.save()
    return redirect(f"/{bookId}/show")

def deleteBook(request, bookId):
    if('userId' not in request.session):
        messages.error(request, "Oops! Login Required to be here! Please log in or Register.")
        return redirect('/')
    if request.method == 'POST':
        thisBook = Book.objects.get(id=bookId)
        user = User.objects.get(id=request.session['userId'])
        if user.id == thisBook.uploadedBy.id:
            thisBook.delete()
    return redirect("/dashboard")

def favOrUnfavBook(request, bookId):
    if('userId' not in request.session):
        messages.error(request, "Oops! Login Required to be here! Please log in or Register.")
        return redirect('/')
    thisBook = Book.objects.get(id=bookId)
    user = User.objects.get(id=request.session['userId'])
    if user in thisBook.usersWhoFavorite.all():
        thisBook.usersWhoFavorite.remove(thisBook)
    else:
        thisBook.usersWhoFavorite.remove(thisBook)
    
    
    return redirect(f'/{bookId}/show')

def myBooks(request, userId):
    if('userId' not in request.session):
        messages.error(request, "Oops! Login Required to be here! Please log in or Register.")
        return redirect('/')
    user = User.objects.get(id=request.session['userId'])
    myBooks = Book.objects.filter(uploadedBy=user)
    context = {
        "user":user,
        "myBooks":myBooks,
    }
    return render(request, "myBooks.html", context)        
