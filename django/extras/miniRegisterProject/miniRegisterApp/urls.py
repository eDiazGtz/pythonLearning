from django.urls import path
from .views import landing, dashboard, register

urlpatterns = [
    path('', landing, name='landing'),
    path('dashboard', dashboard, name='dashboard'),
    path('register', register, name='register'),
]
