from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/',views.about),
    path('courses/',views.courses),
    path('contact/',views.contact)


]