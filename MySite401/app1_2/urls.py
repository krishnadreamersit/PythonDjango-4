
from django.contrib import admin
from django.urls import path
from app1_2 import views

urlpatterns = [
    path('index', views.index), # 127.0.0.1:800/app1_2/index
]