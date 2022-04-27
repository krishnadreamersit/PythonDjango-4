from django.contrib import admin
from app4_1.models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','address')
