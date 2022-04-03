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


def update_form(request):
    # display update form
    eid = int(request.GET.get('eid'))
    email = Email.objects.get(id=eid) # Record Search - on database using Model
    context = {'email': email}
    return render(request, 'app2_2/update_form.html', context)


def update_email(request):
    # read values from url
    ID = request.POST.get('txtID')
    txtEmail = request.POST.get('txtEmail')
    email = Email.objects.get(id=ID)# search email
    email.email=txtEmail # set new email
    email.save() # save email
    return HttpResponseRedirect('./emails')


def delete_form(request):
    # display update form
    eid = int(request.GET.get('eid'))
    email = Email.objects.get(id=eid)  # Record Search - on database using Model
    context = {'email': email}
    return render(request, 'app2_2/delete_form.html', context)


def delete_email(request):
    # read values from url
    ID = request.POST.get('txtID')
    email = Email.objects.get(id=ID)# search email
    email.delete() # save email
    return HttpResponseRedirect('./emails')