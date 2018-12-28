from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # url(r'^$', views.index),
    # url(r'^new/$', views.new),
    # url(r'^create$', views.create),
    # url(r'^')
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:number>/', views.show),
    path('<int:number>/edit/', views.edit),
    path('<int:number>/delete/', views.destroy),
]