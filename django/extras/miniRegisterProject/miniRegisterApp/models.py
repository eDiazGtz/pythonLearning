from django.core.exceptions import ValidationError
from django.db import models
from django.forms import ModelForm

# Create your models here.

class UserManager(models.Manager):
    def createValidator(self, postData):
        errors = {}
        if len(postData['firstName']) < 1:
            errors["firstName"] = "First Name should be at least 1 character"
        if len(postData['lastName']) < 1:
            errors["lastName"] = "Last Name should be at least 1 character"
        if len(postData['email']) > 50:
            errors["email"] = "Email max length 50 Characters"
        return errors

class User(models.Model):
    firstName = models.CharField(max_length=17)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    objects = UserManager()



