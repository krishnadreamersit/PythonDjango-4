# Calling 3rd Party's REST-API
    # http://dummy.restapiexample.com/api/v1/employees # Display All
    # http://dummy.restapiexample.com/api/v1/employee/3/ # Search Record

# Display All Records
import requests # pip install requests
import json
# url = "http://dummy.restapiexample.com/api/v1/employees/"
url = "https://fakestoreapi.com/products"

# Select All
def all():
    response = requests.get(url)
    if response.status_code ==200:
        records = json.loads(response.content) # Text to Dictionary
        return records
    else:
        return None

# Search Record based on ID
def get(id):
    response = requests.get(url+"/"+str(id))
    if response.status_code ==200:
        records = json.loads(response.content) # Text to Dictionary
        return records
    else:
        return None

# Test
# Select All
# records = all()
# # print(records)
# for record in records:
#     print(record)
#     print()

# Search Record based on ID
# record = get(1)
# if record!=None:
#     print(record)
# else:
#     print("Record not found!")

# Apply in Web App, Mobile App, Desktop, Console App
    # Console -> cmd
    # Desktop -> tkinter

# Task - Console
    # Insert new record
    # Update/Edit existing record