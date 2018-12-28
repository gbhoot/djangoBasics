from django.urls import path
from . import views

urlpatterns = [
    path('users', views.index),
    path('users/new/', views.register),
    path('login', views.login),
    path('register', views.register),
]