from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('demo/',views.demo),
    path('save/',views.save,name='save')
]