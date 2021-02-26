from django.urls import path
from .views import landing, dojo

urlpatterns = [
    path('', landing, name="landing"),
    path('dojo', dojo, name="dojo"),
]
