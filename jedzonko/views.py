from datetime import datetime
from random import shuffle
from typing import List

from django.shortcuts import render
from django.views import View
from jedzonko.models import Recipe, Plan

from jedzonko.models import Recipe


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)

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

