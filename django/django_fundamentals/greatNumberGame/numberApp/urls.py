from django.urls import path
from .views import home, assign, game, processGame

urlpatterns = [
    path('', home, name="home"),
    path('assignUsername', assign),
    path('game', game),
    path('processGame', processGame)
]