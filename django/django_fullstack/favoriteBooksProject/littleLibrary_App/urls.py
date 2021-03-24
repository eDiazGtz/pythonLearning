from django.urls import path
from .views import landing, dashboard, register, login, logout, newBook, showBook, updateBook, deleteBook, favOrUnfavBook, myBooks

urlpatterns = [
    path('', landing, name='landing'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('dashboard', dashboard, name='dashboard'),
    path('logout', logout, name='logout'),
    path('newBook', newBook, name='newBook'),
    path('<int:bookId>/show', showBook, name='showBook'),
    path('<int:bookId>/update', updateBook, name='updateBook'),
    path('<int:bookId>/destroy', deleteBook, name='deleteBook'),
    path('<int:bookId>/favorite', favOrUnfavBook, name='favoriteBook'),
    path('<int:userId>', myBooks, name='myBooks'),
]
