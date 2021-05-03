from django.db import models

# Create your models here.

class Ninja(models.Model):
    name = models.CharField(max_length=17)
    wallet = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Doge(models.Model):
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Nyan(models.Model):
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Location(models.Model):
    goldMade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    #Different Kinds of Coins?
    # nyanCoin - 2 nyanCoin = 1 Doge Coin

