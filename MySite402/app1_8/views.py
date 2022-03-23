from django.shortcuts import render

# Create your views here.


# Display webform
def display_form(request):
    return render(request, 'app1_8/form1.html')


# Getting value from webform - get method
def get_form(request):
    tmpName = request.GET['txtName']
    context = {'name':tmpName}
    return render(request, 'app1_8/index.html', context)


# Getting value from webform - post method
def get_form2(request):
    tmpName = request.POST['txtName']
    context = {'name':tmpName}
    return render(request, 'app1_8/index.html', context)
