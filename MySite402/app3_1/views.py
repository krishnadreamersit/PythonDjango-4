from django.http import HttpResponse
from django.shortcuts import render
from app3_1.forms import Form1
from app3_1.forms import Form2

from app3_1.models import Model1
from app3_1.models import Model2


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


def form2(request):
    # display form, receive form
    if(request.method=='GET'):
        # Display form
        f2 = Form2()
        return render(request, 'app3_1/form2.html', {'form': f2})
    elif(request.method=='POST'):
        # Receive value
        nid = request.POST['nid']
        ntitle = request.POST['title']
        ncontent = request.POST['content']
        # Process(Validation)
        
        # Save
        obj2 = Model2(nid=nid, title=ntitle, content=ncontent)
        obj2.save()
        str1 = "<h3>Record Save Successfully</h3>"
        str1 = str1+"<p><a href='./form2'>New Entry</a></p>"
        return HttpResponse(str1)

