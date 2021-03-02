from django.urls import path
from .views import index, new, create, show, edit, destroy

urlpatterns = [
    path('', index), #/
    path('new', new), #/new
    path('create', create), #/create
    path('<int:number>', show), #/number --- /7
    path('<int:number>/edit', edit), #/number/edit --- /4/edit
    path('<int:number>/delete', destroy), #/number/delete --- /4/delete
]
