"""scrumlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from jedzonko.views import IndexView, App_recpies
from jedzonko import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', IndexView.as_view),

    # path("", views.karuzela),
    # path('main/', views.dashboard),
    path('plan/list/', views.plan_list),
    path("", views.karuzela),  # Karuzela na stronie tytułowej
    path('main/', views.dashboard),

    # path('recipe/list/', App_recpies.as_view()),
    path('', views.landing_page),
    # path('recipe/<int:id>/', views.recipe_details),

    # path('', views.landing_page),

    # path('recepie/list/', App_recpies.as_view),
    path('recipie/list/', views.as_view),
    path('recipie/<int:id>/', views.recipe_details),

    # path('recipe/add/', views.app_add_recipe),
    path('recipe/modify/<int:id>/', views.app_edit_recipe),

    path('plan/<int:id>/', views.app_details_schedules),
    # path('plan/add/', views.add_app_add_schedules),

    # path('plan/add-recipe/', views.app_schedules_meal_recipe),
    path('plan/add-recipe/', views.plan_details),

    # path('plan/list/', views.app_schedules),

    # path('plan/add-recepie/', views.app_schedules_meal_recipe),
    # path('plan/list/', views.app_schedules),

    # path('test', views.last_plan)

    # path('plan/list/', views.app_schedules),
    path('recipe/add/', views.new_recipe),
    path('plan/add/', views.new_plan),
]
