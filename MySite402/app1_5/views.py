from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'app1_5/index.html')