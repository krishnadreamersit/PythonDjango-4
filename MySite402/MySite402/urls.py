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

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.default), # Default Url Pattern # http://localhost:8000 or http://127.0.0.1:8000
    path('index', views.index), # http://127.0.0.1:8000/index
    path('home/', views.home), # http://127.0.0.1:8000/home/
    path('app1_1/', include('app1_1.urls')),
    path('app1_2/', include('app1_2.urls')),
    path('app1_3/', include('app1_3.urls')),
    path('app1_4/', include('app1_4.urls')),
    path('app1_5/', include('app1_5.urls')), # testing bootstrap library
    path('app2_3/', include('app1_6.urls')), # bootstrap one page site
    path('app1_7/', include('app1_7.urls')), # sending value from url
    path('app1_8/', include('app1_8.urls')), # sending value from webfrom
    path('app1_9/', include('app1_9.urls')), # ePanel
    path('app2_1/', include('app2_1.urls')), # Model
    path('app2_2/', include('app2_2.urls')), # Model CRUD App-1
    path('app2_3/', include('app2_3.urls')), # CMS using Model
    path('app3_1/', include('app3_1.urls')), # Form
    path('app4_1/', include('app4_1.urls')), # ModelForm
    path('app5_1/', include('app5_1.urls')), # TemplateLanguage
    path('admin/', admin.site.urls), # http://127.0.0.1:8000/admin/
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)