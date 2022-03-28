from django.contrib import admin
from app2_1.models import Person # Step-1
from app2_1.models import Person2
from app2_1.models import Country

# Register your models here.

admin.site.register(Person) # Step-2
admin.site.register(Person2)
admin.site.register(Country)