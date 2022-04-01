from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Email

def index(request):
    return render(request, "app2_2/index.html")

def gmail_email(request):
    tmpEmail = request.POST['email'] # Receive value form Webform
    email = Email() # Create an object of Model
    email.email = tmpEmail # Assign/Initialize email
    email.save() # Save data on database using an object of Model
    return HttpResponseRedirect('emails') # redirect to url pattern

def display_emails(request):
    emails = Email.objects.all() # Get all records using Model
    context = {'emails':emails}
    return render(request, 'app2_2/emails.html', context) # redirect to template