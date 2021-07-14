from django.urls import path
from .views import root, findgold, reset

urlpatterns = [
    path('', root, name="root"),
    path('findgold', findgold, name="findgold"),
    path('reset', reset, name="reset"),
]
