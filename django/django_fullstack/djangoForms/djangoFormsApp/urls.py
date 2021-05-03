from django.urls import path
from .views import landing, dashboard, register, do_login, logout, createDragon

urlpatterns = [
    path('', landing, name='landing'),
    path('register', register, name='register'),
    path('login', do_login, name='login'), #changed the name of LOGIN for django Login method in views.py
    path('dashboard', dashboard, name='dashboard'), #added another comment
    path('logout', logout, name='logout'),
    path('dragon/create', createDragon),
    
]
