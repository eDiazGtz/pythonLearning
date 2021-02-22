from django.urls import path
from .views import root, result

urlpatterns = [
    path('', root, name="root"),
    path('result', result, name="result"),
]
