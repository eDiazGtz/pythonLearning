from django.urls import path
from .views import redirectLanding

urlpatterns = [
    path('', redirectLanding, name="redirectLanding"),
]