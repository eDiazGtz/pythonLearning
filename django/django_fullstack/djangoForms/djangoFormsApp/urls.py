from django.urls import path
from .views import landing, dashboard, register, do_login, logout, createDragon

urlpatterns = [
    path('', landing, name='landing'),
    path('register', register, name='register'),
    path('login', do_login, name='login'), #I want a comment now
    path('dashboard', dashboard, name='dashboard'),
    path('logout', logout, name='logout'),
    path('dragon/create', createDragon),
    
]
