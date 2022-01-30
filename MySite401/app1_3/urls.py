
from django.contrib import admin
from django.urls import path
from app1_3 import views

urlpatterns = [
    path('display_form', views.display_form1), # 127.0.0.1:800/app1_3/display_form
    path('calculate', views.calculate),
]