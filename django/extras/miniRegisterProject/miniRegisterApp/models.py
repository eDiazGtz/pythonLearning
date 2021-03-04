from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

def validateLengthGreaterThanTwo(value):
    if len(value) < 2:
        raise ValidationError(
            '{} must be longer than: 1'.format(value)
        )

class UserManager(models.Manager):
    def basicValidator(self, postData):
        errors = {}
        if len(postData['firstName']) < 1:
            errors["firstName"] = "First Name should be at least 1 character"
        if len(postData['lastName']) < 1:
            errors["lastName"] = "Last Name should be at least 1 character"
        if len(postData['email']) > 50:
            errors["email"] = "Email max length 50 Characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=17, validators = [validateLengthGreaterThanTwo])
    last_name = models.CharField(max_length=20, validators = [validateLengthGreaterThanTwo])
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
