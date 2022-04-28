from django.shortcuts import render
# Create your views here.

def index(request):
    # Step-1 : read value
        # declare and initialize variable (local value)
        # receive value from URL
        # receive value from WebForm
        # read value from file(s) -> notepad, word, excel, pdf, xml, csv etc
        # read value from database (rdbms, nosql)

    # declare and initialize variable (local value)
    fullName = "John bista" # Static value

    # Step-2: Processing
        # No processing (A & L)

    if(fullName=='John Bista'):
        fullName='Jatain Singh'

    # Step-3: Send to template
    values = {'name': fullName} # Container

    # HTML Template
        # {{ key of dictionary }} # Display
        # {{ name | upper }} # Display with Filter
        # {% %} # Tag (Python Programming)
    return render(request, 'app5_1/index.html', values)