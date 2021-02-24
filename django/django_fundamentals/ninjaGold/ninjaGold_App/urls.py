from django.urls import path
from .views import root, findgold

urlpatterns = [
    path('', root, name="root"),
    path('findgold', findgold, name="findgold"),
]
