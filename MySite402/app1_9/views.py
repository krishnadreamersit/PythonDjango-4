from django.shortcuts import render
from django.http import HttpResponse
from core import database

# Create your views here.

def emails(request):
    # connect with db and get all subscribes emails
    emails = database.select_all()
    print(emails)

    # send emails to display on template
    context = {'emails':emails}
    return render(request, 'app1_9/index.html', context)