from django.urls import path
from .views import index, new, create, show, edit, destroy

urlpatterns = [
    path('', index, name="index"), #/
    path('new', new, name="new"), #/new
    path('create', create, name="create"), #/create
    path('<int:number>', show, name="show"), #/number aka /15
    path('<int:number>/edit', edit, name="edit"), #/edit
    path('<int:number>/delete', destroy, name="delete"), #/15/delete
]