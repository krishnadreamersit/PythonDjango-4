from django.shortcuts import render

# Step-1 Library Import
from django.http import HttpResponse

# Create your views here.
# Step-2 Create view function
def hello(request):
    return HttpResponse("Hello world of django!")


def welcome(request):
    str1 ="""
    <h1>Building Global IT Professionals since 2008</h1>
    <h4>AN ISO 9001:2015 CERTIFIED IT LEARNING CENTER</h4>
    <p>Broadway Infosys Nepal is one of the best inclusive computer training institutes in Kathmandu, Nepal. Established in 2008, our professional IT Training and Development center has been employing experts in this field to impart professional education.</p>
    """
    return HttpResponse(str1)

def placement(request):
    # return HttpResponse("Hello from Placement")
    # Load html file and return
    return render(request, 'app1_1/placements.html')