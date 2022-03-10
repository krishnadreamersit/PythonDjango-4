from django.urls import path
# 1. import view
from . import views

urlpatterns = [
    path('index', views.index), # http://127.0.0.1:8000/index
    path('home/', views.home), # http://127.0.0.1:8000/home/
]