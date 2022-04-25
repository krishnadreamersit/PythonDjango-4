from django.shortcuts import render
from app3_1.forms import Form1
from app3_1.models import Model1

def index(request):
    persons = Model1.objects.all()
    context = {'persons': persons}
    return render(request, 'app3_1/index.html', context)


def display_form(request):
    form1 = Form1()
    context = {'form1': form1}
    return render(request, 'app3_1/display_form.html', context)


def get_form(request):
    # receive form data
    id = request.GET.get('id')
    name = request.GET['name']
    address = request.GET.get('address')

    # validation and processing
    mode1 = Model1()
    mode1.id=id
    mode1.name=name
    mode1.address=address
    mode1.save()

    # redirect to html template
    context = {'id': id, 'name':name, 'address':address}
    return render(request, 'app3_1/get_form.html', context)