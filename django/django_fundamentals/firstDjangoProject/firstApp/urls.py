from django.urls import path
from .views import root, newBlog, createBlog, showBlog, editBlog, deleteBlog

urlpatterns = [
    path('', root, name="root"),
    path('new', newBlog, name="newBlog"),
    path('create', createBlog, name="createBlog"),
    path('<int:blog_id>', showBlog, name="showBlog"),
    path('<int:blog_id>/edit', editBlog, name="editBlog"),
    path('<int:blog_id>/delete', deleteBlog, name="deleteBlog"),
]
