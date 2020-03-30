from datetime import datetime
from random import shuffle
from typing import List
from django.shortcuts import render, redirect
from django.views import View
from jedzonko.models import Recipe, Plan



class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "app-recipes.html", ctx)

    def index1(request):
        return render(request, 'index.html')


def dashboard(request):
    return render(request, "dashboard.html")



def count_plan(request):
    count_plan = Plan.objects.all().count()
    return render(request, 'dashboard.html', {'count_plan':count_plan})

def karuzela(request):
    recepises = list(Recipe.objects.all())
    shuffle(recepises)
    recipe1 = recepises[0]
    recipe2 = recepises[1]
    recipe3 = recepises[2]
    return render(request, "index.html", {"recipe1": recipe1, "recipe2": recipe2, "recipe3": recipe3})

def new_recipe(request):
    if request.method == "GET":
        return render(request, "app-add-recipe.html")
    elif request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        preparation_time = request.POST["preparation_time"]
        ingredients = request.POST["ingredients"]
        message = "Wypełnij poprawnie wszystkie pola"
        if len(name) == 0 or len(description) == 0 or len(ingredients) == 0 or preparation_time == 0:
            return render(request, "app-add-recipe.html", {'message': message})
        else:
            Recipe.objects.create(name=name, description=description, preparation_time=preparation_time, ingredients=ingredients, votes=0)
            return redirect('/recipe/list/')
# do przedyskutowania podejscie do sposobu przygotowania w Postgres SQl

def new_plan(request):
    if request.method == "GET":
        return render(request, "app-add-schedules.html")
    elif request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        message = "Wypełnij poprawnie wszystkie pola"
        if len(name) == 0 or len(description) == 0:
            return render(request, "app-add-schedules.html", {'message': message})
        else:
            Plan.objects.create(name=name, description=description)
            return redirect('/plan/<INT:id>/details')



class App_recpies(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "app-recipes.html", ctx)

def Summary_Recipies(request):
    summary = Recipe.objects.all().count()
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

