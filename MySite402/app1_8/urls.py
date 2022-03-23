from django.urls import path
from . import views
urlpatterns = [
    path('display_form', views.display_form),
    path('get_form', views.get_form),
    path('get_form2', views.get_form2),
]