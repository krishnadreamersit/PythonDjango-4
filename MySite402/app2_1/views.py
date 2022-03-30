from django.shortcuts import render
from django.http import HttpResponse
from .models import Country
from .models import Person2

# Create your views here.


def index(request):
    countries = Country.objects.all()
    for country in countries:
        print(country)
        break
    context = {'countries': countries}
    return render(request, 'app2_1/index.html',context)


def crud(request):
    # C -> Create (Insert New Record)
    # Step-1
    # p1 = Person2()
    # p1.pid=1
    # p1.fullName="Jatin Singh"
    # p1.contactAddress="KTM"
    # p1.save()

    # Step-2
    # p2 = Person2(pid=2, fullName='John Bista', contactAddress='LAT')
    # p2.save()

    # R -> Retrieve
    # persons = Person2.objects.all() # all records
    # for person in persons:
    #     print(person)

    # Select all records
    """
    countries = Country.objects.all() # all records
    for country in countries:
        print(country)
    """

    # Search record
    # countries = Country.objects.filter(country='Nepal')
    # countries = Country.objects.filter(country='India')
    # countries = Country.objects.filter(country__startswith='M')
    # for country in countries:
    #     print(country)

    # Update
    # p1 = Person2.objects.get(pid=2)
    # print(p1) # 2, John Bista, LAT
    # p1.contactAddress="Lalitpur"
    # p1.save()
    # p1 = Person2.objects.get(pid=2)
    # print(p1)  # 2, John Bista, Lalitpur

    # Delete Record
    # p1 = Person2.objects.get(pid=1)
    # p1.delete()

    return HttpResponse("Hello from CRUD")