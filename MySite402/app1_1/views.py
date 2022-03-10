from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    response = HttpResponse("Hello from index of app1_1") # Return Text
    return response


def home(request):
    return render(request, 'app1_1/index.html') # Return HTML File