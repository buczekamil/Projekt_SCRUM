from django.db import models



# Create your models here.


class Recipe (models.Model):
    name = models.CharField(max_length=64)
    ingredients = models.CharField(max_length=300)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    preparation_time = models.IntegerField()
    votes = models.IntegerField(default=0)

class Plan (models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

