from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', views.post_list, name='post_list'),
]