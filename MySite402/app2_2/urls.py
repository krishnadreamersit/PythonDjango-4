from django.urls import path
from . import views
urlpatterns = [
    path('', views.index), # Home Page -> default
    path('get_email', views.gmail_email), # 1 Email Receive and Save
    path('emails', views.display_emails), # 2 Display all emails
]