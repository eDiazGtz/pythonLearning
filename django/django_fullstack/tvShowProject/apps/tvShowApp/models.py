from django.db import models

# Create your models here.
class TvShow(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    releaseDate = models.DateTimeField()
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
