from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    #tmpName = request.GET.get('name') # getting value
    tmpName = request.GET['name']  # getting value
    print("Hello: "+tmpName) # Redirect to terminal
    #return HttpResponse("Hello: "+tmpName) # Redirect to browser

    # Sending value to template
    context = {'name':tmpName}
    return render(request, 'app1_7/index.html', context)

