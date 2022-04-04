from django.contrib import admin
from app2_1.models import Person # Step-1
from app2_1.models import Person2
from app2_1.models import Country

from app2_1.models import Model1
from app2_1.models import Model2

from app2_1.models import Place
from app2_1.models import Restaurant

# Register your models here.

admin.site.register(Person) # Step-2
admin.site.register(Person2)
admin.site.register(Country)
admin.site.register(Model1)
admin.site.register(Model2)
admin.site.register(Place)
admin.site.register(Restaurant)