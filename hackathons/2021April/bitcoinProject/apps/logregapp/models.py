from django.db import models
import re


# Create your models here.

class UserManager(models.Manager):
    def createValidator(self, postData):
        errors = {}
        if len(postData['name']) < 10:
            errors["name"] = "Name must be longer than 10 characters."
                
        if len(postData['password']) < 8:
            errors["password"] = "Password must at least 7 characters."
        
        if postData['password'] != postData['passwordConfirm']:
            errors["passwordConfirm"] = "Passwords do not match."

        return errors

class User(models.Model):
    name = models.CharField(max_length=17)
    wallet = models.IntegerField()
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

