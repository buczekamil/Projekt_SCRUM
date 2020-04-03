from datetime import datetime
from random import shuffle
from django.http import Http404, HttpResponse
from typing import List
import datetime
from django.shortcuts import render, redirect
from django.views import View
from jedzonko.models import Recipe, Plan, RecepiePlan, DayName
from django.core.paginator import Paginator, EmptyPage, InvalidPage


class IndexView(View):

    # def get(self, request):
    #     ctx = {"actual_date": datetime.now()}
    #     return render(request, "app-recipes.html", ctx)

    def as_view(request):
        return render(request, 'index.html')


def dashboard(request):
    count_plan = Plan.objects.all().count()
    summary = Recipe.objects.all().count

    last_plan = list(Plan.objects.all().order_by('created'))[-1]
    recipes = last_plan.recepieplan_set.all()

    recipes_lst = []

    for i in range(1, 8):
        tmp = recipes.filter(day_name=i)
        if tmp:
            recipes_lst.append(tmp.order_by('order'))

    return render(request, 'dashboard.html',
                  {'count_plan': count_plan, 'last_plan': last_plan, 'summary_recipes': summary,
                   'recipes_lst': recipes_lst})


def karuzela(request):
    recepises = list(Recipe.objects.all())
    shuffle(recepises)
    recipe1 = recepises[0]
    recipe2 = recepises[1]
    recipe3 = recepises[2]
    return render(request, "index.html", {"recipe1": recipe1, "recipe2": recipe2, "recipe3": recipe3})


def plan_list(request):
    plans_list = Plan.objects.all().order_by("name")
    paginator = Paginator(plans_list, 50)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        plans = paginator.page(page)
    except(EmptyPage, InvalidPage):
        plans = paginator.page(page)

    return render(request, "app-schedules.html", {"plans": plans})


def new_recipe(request):
    if request.method == "GET":
        return render(request, "app-add-recipe.html")
    elif request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        preparation_time = request.POST["preparation_time"]
        ingredients = request.POST["ingredients"]
        preparation_details = request.POST["preparation_details"]
        message = "Wypełnij poprawnie wszystkie pola"
        if len(name) == 0 or len(description) == 0 or len(ingredients) == 0 or int(preparation_time) == 0:
            return render(request, "app-add-recipe.html", {'message': message})
        else:
            Recipe.objects.create(name=name, description=description, preparation_time=preparation_time,
                                  preparation_details=preparation_details, ingredients=ingredients, votes=0)
            return redirect('/recipe/list/')


def new_plan(request):
    if request.method == "GET":
        return render(request, "app-add-schedules.html")
    elif request.method == "POST":
        name = request.POST["name"]
        id = request.POST.get("id")
        description = request.POST["description"]
        message = "Wypełnij poprawnie wszystkie pola"
        if len(name) == 0 or len(description) == 0:
            return render(request, "app-add-schedules.html", {'message': message})
        else:
            Plan.objects.create(name=name, description=description)
            return redirect(f"/plan/list/")


def plan_details(request):
    days = DayName.objects.all()
    plans = Plan.objects.all()
    recipes = Recipe.objects.all()
    if request.method == "GET":
        return render(request, 'add-schedules-meal-recipe.html', {'plans': plans, 'recipes': recipes, 'days': days})
    elif request.method == "POST":
        plan = request.POST["plan"]
        order = request.POST["order"]
        meal_name = request.POST["meal_name"]
        recipe = request.POST["recipe_name"]
        day = request.POST["day"]
        message = "Wypełnij poprawnie wszystkie pola"
        if len(meal_name) == 0 or len(order) == 0:
            return render(request, 'add-schedules-meal-recipe.html', {'message': message})
        else:
            plan2 = Plan.objects.get(name=plan)
            plan_id = plan2.id
            recipe2 = Recipe.objects.get(name=recipe)
            recipe_id = recipe2.id
            day2 = DayName.objects.get(name=day)
            day_id = int(day2.id)
            RecepiePlan.objects.create(meal_name=meal_name,
                                       order=order,
                                       day_name_id=day_id,
                                       plan_id=plan_id,
                                       recipe_id=recipe_id)
            return redirect('/plan/add-recipe/')


def recipe_modify(request, id):
    id = id
    if request.method == "GET":
        try:
            recipe = Recipe.objects.get(id=id)
            return render(request, "app-edit-recipe.html", {'recipes': [recipe]})
        except Recipe.DoesNotExist:
            raise Http404
    elif request.method == "POST":
        name = request.POST["name"]
        preparation_time = request.POST["preparation_time"]
        ingredients = request.POST["ingredients"]
        description = request.POST["description"]
        updated_date = datetime.date.today()
        preparation_details = request.POST["preparation_details"]

        # id = request.POST.get("id")
        message = "Wypełnij poprawnie wszystkie pola"
        recipe = Recipe.objects.get(id=id)
        if len(name) ==0 or len(ingredients) ==0 or len(description) ==0 or len(preparation_details) ==0 or int(preparation_time) ==0:

            return render(request, 'app-edit-recipe.html', {'message':message, 'recipes':[recipe]})
        else:
            Recipe.objects.filter(id=id).update(name=name,
                                                preparation_time=preparation_time,
                                                ingredients=ingredients,
                                                description=description,
                                                updated=updated_date,
                                                preparation_details=preparation_details)
            return redirect(f"/recipe/modify/{id}")



class App_recpies(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "app-recipes.html", ctx)


def as_view(request):
    recipies_list = Recipe.objects.all().order_by("-votes")
    # return render(request, "app-recipes.html", {"recipies": recipies_list})
    paginator = Paginator(recipies_list, 50)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        recipies = paginator.page(page)
    except(EmptyPage, InvalidPage):
        recipies = paginator.page(page)

    return render(request, "app-recipes.html", {"recipies": recipies})


def landing_page(request):
    return render(request, 'landing_page.html')


def recipe_details(request, id):
    recipe_detail = Recipe.objects.get(id=id)
    if request.method == "GET":
        return render(request, 'app-recipe-details.html', {'recipe_detail': recipe_detail})
    elif request.method == "POST" and str(request.POST.get("like")):
        vote_add_1 = int(recipe_detail.votes) + 1
        Recipe.objects.filter(id=id).update(votes=vote_add_1)
        return redirect(f'/recipe/{id}/')
    else:
        votes = recipe_detail.votes
        vote_add_1 = int(votes - 1)
        if vote_add_1 >0 :
            Recipe.objects.filter(id=id).update(votes=vote_add_1)
            return redirect(f'/recipe/{id}/')
        else:
            Recipe.objects.filter(id=id).update(votes=0)
            return redirect(f'/recipe/{id}/')


def app_add_recipe(request):
    return render(request, 'app-add-recipe.html')


def app_edit_recipe(request):
    return render(request, 'app-add-recipe.html')




def app_details_schedules(request, id):
    plan = Plan.objects.get(id=id)
    recipes = plan.recepieplan_set.all()
    recipes_lst = []
    for i in range(1, 8):
        tmp = recipes.filter(day_name=i)
        if tmp:
            recipes_lst.append(tmp.order_by('order'))
    if request.method == 'POST':
        meal_id = request.POST['id']
        RecepiePlan.objects.get(id=meal_id).delete()
        return render(request, 'app-details-schedules.html',
                      {'plan': plan, 'recipes_lst': recipes_lst})
    else:
        return render(request, 'app-details-schedules.html',
                       {'plan': plan, 'recipes_lst': recipes_lst})


def add_app_add_schedules(request):
    return render(request, 'app-add-schedules.html')


def app_schedules_meal_recipe(request):
    return render(request, 'app-schedules-meal-recipe.html')


def app_schedules(request):
    return render(request, 'app-schedules.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')