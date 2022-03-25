from django.urls import path
from . import views
urlpatterns = [
    path('emails', views.emails),
]