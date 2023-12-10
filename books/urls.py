# coding=utf-8


from django.urls import re_path as url, include, path
from . import views

urlpatterns = [
    path('', views.index),
    url('index/', views.index),
    url('home/', views.home),
    url('add/', views.add),
    url('edit/', views.edit),
    url('delete/', views.delete),
    url('me/', views.to_me),
    url('borrow/', views.index_borrow)
]
