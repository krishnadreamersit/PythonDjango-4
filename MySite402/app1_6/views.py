from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
from app1_6 import database

def index(request):
    return render(request, "app1_6/index.html")

# Step-2
def gmail_email(request):
    # Step-3 Receive value
    tmpEmail = request.POST['email']
    print(tmpEmail)
    # process -> insert on db table
    # database.create_table()
    result = database.insert_record(tmpEmail)
    if result==True:
        print("Insert record successfully")
    else:
        print("Error to insert record")
    return HttpResponseRedirect('emails') # redirect to url pattern

def display_emails(request):
    emails = database.select_all()
    print(emails)
    return HttpResponse(emails)