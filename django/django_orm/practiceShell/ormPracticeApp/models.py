from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    emailAddress = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Dojo(models.Model):
    name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)

class Ninja(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas",on_delete=models.CASCADE)
