from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        "books":books,
    }
    return render(request, "index.html", context)

def createBook(request):
    if request.method == 'POST':
        Book.objects.create(title=request.POST['title'],description=request.POST['description'])
        return redirect("/")
    return redirect("/")

def showBook(request, bookId):
    thisBook = Book.objects.get(id=bookId)
    allAuthors = Author.objects.all()
    context = {
        "thisBook" : thisBook,
        "allAuthors" : allAuthors,
    }
    return render(request, "showBook.html", context)

def addAuthor(request):
    bookId = request.POST['bookId']
    authorId = request.POST['authorId']
    thisBook = Book.objects.get(id=bookId)
    thisAuthor = Author.objects.get(id=authorId)
    #join together
    thisBook.myAuthors.add(thisAuthor)
    return redirect(f"/books/{bookId}")


def newAuthor(request):
    authors = Author.objects.all()
    context = {
        "authors":authors
    }
    return render(request, "newAuthor.html", context)

def createAuthor(request):
    if request.method == 'POST':
        Author.objects.create(firstName=request.POST['firstName'],lastName=request.POST['lastName'],notes=request.POST['notes'])
        return redirect("/newAuthor")
    return redirect("/newAuthor")

def showAuthor(request, authorId):
    thisAuthor = Author.objects.get(id=authorId)
    allBooks = Book.objects.all()
    context = {
        "thisAuthor" : thisAuthor,
        "allBooks" : allBooks,
    }
    return render(request, "showAuthor.html", context)

def addBook(request):
    bookId = request.POST['bookId']
    authorId = request.POST['authorId']
    thisBook = Book.objects.get(id=bookId)
    thisAuthor = Author.objects.get(id=authorId)
    #join together
    thisAuthor.myBooks.add(thisBook)
    return redirect(f"/authors/{authorId}")

