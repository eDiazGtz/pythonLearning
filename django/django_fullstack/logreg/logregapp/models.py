from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=17)
    email = models.CharField(max_length=50)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)