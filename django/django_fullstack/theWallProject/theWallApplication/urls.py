from django.urls import path
from .views import landing, dashboard, register, login, logout, newPost, newComment, destroyPost, destroyComment

urlpatterns = [
    path('', landing, name='landing'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('dashboard', dashboard, name='dashboard'),
    path('logout', logout, name='logout'),
    path('newPost', newPost, name='newPost'),
    path('newComment', newComment, name='newComment'),
    path('destroyPost/<int:postId>', destroyPost, name='destroyPost'),
    path('destroyComment/<int:commentId>', destroyComment, name='destroyComment'),
]