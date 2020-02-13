from django.contrib import admin
from django.urls import path
from general import urls
from . import views


urlpatterns = [
    path('home/', views.home, name="home_page"),
]
