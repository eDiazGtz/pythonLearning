from django.urls import path
from .views import dashboard, add, deletePage, destroy

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('add', add, name="add"),
    path('destroy', deletePage, name="deletePage"),
    path('destroy/<int:courseId>', destroy, name="destroy"),
]