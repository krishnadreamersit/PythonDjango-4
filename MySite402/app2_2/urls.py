from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index),
    path('get_email', views.gmail_email), # 1
    path('emails', views.display_emails), # 2
]