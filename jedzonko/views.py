from datetime import datetime
from random import shuffle
from typing import List

from django.shortcuts import render, HttpResponse
from django.views import View
from jedzonko.models import Recipe, Plan



class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "app-recipes.html", ctx)

    def as_view(request):
        return render(request, 'index.html')


def dashboard(request):
    count_plan = Plan.objects.all().count()
    last_plan = list(Plan.objects.all().order_by('-created'))[0]
    summary = Recipe.objects.all().count
    return render(request, 'dashboard.html', {'count_plan': count_plan, 'last_plan': last_plan, 'summary_recipes':summary})


def karuzela(request):
    recepises = list(Recipe.objects.all())
    shuffle(recepises)
    recipe1 = recepises[0]
    recipe2 = recepises[1]
    recipe3 = recepises[2]
    return render(request, "index.html", {"recipe1": recipe1, "recipe2": recipe2, "recipe3": recipe3})


class App_recpies(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "app-recipes.html", ctx)

def Summary_Recipies(request):

    return render(request, 'dashboard.html', {'summary_recipes':summary})


def landing_page(request):
    return render(request, 'landing_page.html')


def recipe_details(request):
    return render(request, 'app-recipe-details.html')


def app_add_recipe(request):
    return render(request, 'app-add-recipe.html')


def app_edit_recipe(request):
    return render(request, 'app-edit-recipe.html')


def app_details_schedules(request):
    return render(request, 'app-details-schedules.html'),


def add_app_add_schedules(request):
    return render(request, 'app-add-schedules.html')


def app_schedules_meal_recipe(request):
    return render(request, 'app-schedules-meal-recipe.html')


def app_schedules(request):
    return render(request, 'app-schedules.html')


