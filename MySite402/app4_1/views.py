from django.shortcuts import render
from django.http import HttpResponse
from app4_1.models import Person
from app4_1.forms import PersonForm


def index(request):
    if request.method=='POST':
        person = PersonForm(request.POST)
        if person.is_valid():
            person.save()
    personForm = PersonForm()
    persons = Person.objects.all()
    context = {'form': personForm, 'persons':persons}
    return render(request, 'app4_1/index.html', context)
