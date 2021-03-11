from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validations(self, postData):
        errors = {}
        if len(postData['name']) < 1:
            errors["name"] = "Title should be at least 1 character"
        if len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters"
        elif len(postData['description']) > 255:
            errors["description"] = "Description max 255 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
