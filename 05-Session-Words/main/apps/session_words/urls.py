from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addWord', views.add),
    path('clearSesh', views.clear),
]