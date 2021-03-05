from django.db import models

# Create your models here.

class TvShowManager(models.Manager):
    def createValidator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title must be 2 characters long."
        if len(postData['network']) < 3:
            errors["network"] = "Network must be 3 characters long."
        if len(postData['description']) < 10:
            errors["description"] = "Description must be 10 characters long."
        return errors


class TvShow(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    releaseDate = models.DateTimeField()
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TvShowManager()
