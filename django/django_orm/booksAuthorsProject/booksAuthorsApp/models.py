from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #RELATIONSHIPS
    #myAuthors


class Author(models.Model):
    firstName = models.CharField(max_length=18)
    lastName = models.CharField(max_length=20)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #RELATIONSHIPS
    myBooks = models.ManyToManyField(Book, related_name="myAuthors")
