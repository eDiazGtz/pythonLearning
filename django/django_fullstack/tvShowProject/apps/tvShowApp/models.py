from django.db import models

# Create your models here.
class TvShowManager(models.Manager):
    def basicValidator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors["title"] = "Title should be at least 1 character"
        if len(postData['network']) < 1:
            errors["network"] = "Network should be at least 1 character"
        if len(postData['description']) < 10:
            errors["description"] = "Network should be at least 10 characters"
        elif len(postData['description']) > 255:
            errors["description"] = "Network max 255 characters"
        return errors

class TvShow(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    releaseDate = models.DateTimeField()
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TvShowManager()

