from django.contrib import admin
from app3_1.models import Model1

# Register your models here.
@admin.register(Model1)
class Model1Admin(admin.ModelAdmin):
    list_display = ('id', 'name','address')