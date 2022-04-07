from django.contrib import admin
from .models import SiteTitle
from .models import Banner

# Register your models here.

@admin.register(SiteTitle)
class SiteTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo')