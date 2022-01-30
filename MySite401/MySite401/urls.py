"""MySite401 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Step-1 Import views (app1_1\views.py)
from app1_1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', views.hello), # Step-2 Create url pattern (urlpattern, view function)
    path('welcome', views.welcome), # 127.0.0.1:8000/welcome
    path('placement', views.placement), # 127.0.0.1:8000/placement
    path('app1_2/', include("app1_2.urls")), # 127.0.0.1:800/app1_2/
    path('app1_3/', include("app1_3.urls")), # 127.0.0.1:800/app1_3/
]