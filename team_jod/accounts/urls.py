from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name="Blogs"),
    path('signin', views.login, name="Blogs"),
    path('logout', views.logout, name="Blogs"),



]