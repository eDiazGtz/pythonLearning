from django.urls import path
from .views import landing, processMoney

urlpatterns = [
    path('', landing),
    path('processMoney', processMoney),
]
