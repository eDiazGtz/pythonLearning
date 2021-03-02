from django.urls import path
from .views import landing, new, createShow, showShow, editShow, updateShow, deleteShow

urlpatterns = [
    path('', landing, name="dashboard"), #/shows
    path('new', new, name="newShow"), #shows/new
    path('create', createShow, name="createShow"), #shows/create
    path('<int:show_id>', showShow, name="showShow"), #shows/{id}
    path('<int:show_id>/edit', editShow, name="editShow"), #shows/{id}/edit
    path('<int:show_id>/update', updateShow, name="updateShow"), #shows/{id}/update
    path('<int:show_id>/destroy', deleteShow, name="deleteShow"), #shows/{id}/destroy
]

