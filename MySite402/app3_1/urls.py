from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('display_form', views.display_form),
    path('get_form', views.get_form),
    path('form2', views.form2), # display form, receive form
]