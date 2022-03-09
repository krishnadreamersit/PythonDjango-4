#1. import necessary library
from django.http import HttpResponse


def default(request):
    return HttpResponse("Hello world of Django-1")


def index(request): # create view function (any name) with request parameter (must)
    return HttpResponse("Hello world of Django-2") # return HttpResponse Object


def home(request):
    response = HttpResponse("Hello world of Django-3")
    return response
