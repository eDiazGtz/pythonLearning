from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('assignUsername', views.assign),
    path('game', views.game),
    path('processGame', views.processGame)
]