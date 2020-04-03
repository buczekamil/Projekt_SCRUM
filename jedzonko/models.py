from django.db import models
from enum import Enum


# Create your models here.


class Recipe (models.Model):
    name = models.CharField(max_length=64)
    ingredients = models.CharField(max_length=300)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    preparation_time = models.IntegerField()
    preparation_details = models.CharField(max_length=600, default=None)
    votes = models.IntegerField(default=0)


class DaysOfWeek(Enum):
    Pon = "Poniedziałek"
    Wt = "Wtorek"
    Śro = "Środa"
    Czw = "Czwartek"
    Pt = "Piątek"
    Sob = "Sobota"
    Nie = "Niedziela"

class DayName(models.Model):
    name = models.CharField(max_length=36)
    order = models.IntegerField(unique=True)
# class DayName(models.Model):
#     name = models.CharField(
#         max_length=3, choices=[(tag, tag.value) for tag in DaysOfWeek]
#     )
#     order = models.IntegerField(unique=True)
#
    def __str__(self):
        return self.name

class Plan (models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    recepies = models.ManyToManyField('Recipe', through='RecepiePlan')

    def __str__(self):
        return self.name

class RecepiePlan(models.Model):
    meal_name = models.CharField(max_length=20)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    order = models.IntegerField(unique=True)
    day_name = models.ForeignKey('DayName', on_delete=models.CASCADE)

class Page(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=40)