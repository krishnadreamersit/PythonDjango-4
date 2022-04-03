from django.urls import path
from . import views
urlpatterns = [
    path('', views.index), # Home Page -> default
    path('get_email', views.gmail_email), # 1 Email Receive and Save
    path('emails', views.display_emails), # 2 Display all emails
    path('update_form', views.update_form), # Display Update Form
    path('update_email', views.update_email), # Receive and Update Email
    path('delete_form', views.delete_form),
    path('delete_email', views.delete_email),

]