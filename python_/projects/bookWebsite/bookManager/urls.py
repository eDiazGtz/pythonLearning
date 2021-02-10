from django.urls import path
from .views import index, addBook, seeBook

urlpatterns = [
    path('', index, name='index'),
    path('book', seeBook, name='seeBook'),
    path('addBook', addBook, name='addBook'),
]
