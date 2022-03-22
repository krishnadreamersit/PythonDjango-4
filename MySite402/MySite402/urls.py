"""MySite402 URL Configuration

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
# 1. import view
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.default), # Default Url Pattern # http://localhost:8000 or http://127.0.0.1:8000
    path('index', views.index), # http://127.0.0.1:8000/index
    path('home/', views.home), # http://127.0.0.1:8000/home/
    path('app1_1/', include('app1_1.urls')),
    path('app1_2/', include('app1_2.urls')),
    path('app1_3/', include('app1_3.urls')),
    path('app1_4/', include('app1_4.urls')),
    path('app1_5/', include('app1_5.urls')), # testing bootstrap library
    path('app1_6/', include('app1_6.urls')), # bootstrap one page site
    path('app1_7/', include('app1_7.urls')), # sending value from url

    path('admin/', admin.site.urls), # http://127.0.0.1:8000/admin/
]
urlpatterns += staticfiles_urlpatterns()