from django.shortcuts import render
from django.http import HttpResponse
from .models import Country

# Create your views here.


def index(request):
    countries = Country.objects.all()
    for country in countries:
        print(country)
        break
    context = {'countries': countries}
    return render(request, 'app2_1/index.html',context)
