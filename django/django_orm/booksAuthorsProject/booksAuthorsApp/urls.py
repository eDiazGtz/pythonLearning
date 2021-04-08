from django.urls import path
from .views import index, newAuthor, showBook, showAuthor, createBook, createAuthor, addAuthor, addBook

urlpatterns = [
    path('', index, name="index"),
    path('createBook', createBook, name="createBook"),
    path('newAuthor', newAuthor, name="newAuthor"),
    path('addAuthor', addAuthor, name="addAuthor"),
    path('addBook', addBook, name="addBook"),
    path('createAuthor', createAuthor, name="createAuthor"),
    path('books/<int:bookId>', showBook, name="showBook"),
    path('authors/<int:authorId>', showAuthor, name="showAuthor"),
]
