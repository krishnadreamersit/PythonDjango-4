from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index),
    path('crud', views.crud),
    path('persons', views.display_persons),
]