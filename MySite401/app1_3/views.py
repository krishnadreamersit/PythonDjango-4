from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display_form1(request):
    return render(request, 'app1_3/form1.html')

def calculate(request):
    # receive value
    n1 = request.GET.get('txt_n1') # String -> int
    n2 = request.GET.get('txt_n2') # String -> int
    n3 = int(n1) + int(n2)
    print(n1, n2, n3)
    return HttpResponse("Sum : "+str(n3))