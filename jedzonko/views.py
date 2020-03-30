from datetime import datetime

from django.shortcuts import render
from django.views import View
from jedzonko.models import Recipe, Plan


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