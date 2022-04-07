from django.contrib import admin

from app2_1.models import Person # Step-1
from app2_1.models import Person2
from app2_1.models import Country

from app2_1.models import Model1
from app2_1.models import Model2

from app2_1.models import Place
from app2_1.models import Restaurant
from app2_1.models import Staff

from app2_1.models import Publication
from app2_1.models import Article
# from django.urls.html import format_html

# Register your models here.
# admin.site.register(Person) # Step-2

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # def image(self, obj):
    #     return format_html('<img src="{}"/>'.format(obj.image.url))
    list_display = ('pid', 'fullName','contactAddress', 'photograph')

admin.site.register(Person2)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('cid', 'country','region', 'population', 'area')

admin.site.register(Model1)
admin.site.register(Model2)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Staff)

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'contents')