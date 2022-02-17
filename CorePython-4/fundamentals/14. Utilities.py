# 14 Utilities
    # 14.1 Date & time
    # 14.2 Encryption
    # 14.3 Module, Package
    # 14.4 os Module
    # 14.5 sys Module
    # 14.6 Jupyter NoteBook
    # 14.7 JupyterLab
    # 14.8 Spyder IDE
    # 14.9 Others

# 14.1 Date & Time
# Getting system date and time
from datetime import datetime

current_dt = datetime.now()
currentdt_str = str(current_dt) # dt -> str
print(current_dt) # 2022-02-11 07:48:42.271108
print(type(current_dt)) # <class 'datetime.datetime'>
print(type(currentdt_str)) # <class 'str'>

# Task 14.1
    # Extracting part of datetime
    # 2022-02-11 07:48:42.271108
    # year, month, day, hour, minute, second

# Solution
print(current_dt.year)
print(current_dt.month)
print(current_dt.day)

print(current_dt.hour)
print(current_dt.minute)
print(current_dt.second)
print(current_dt.microsecond)

# Timestamp
# DateTime to TimeStamp
current_dt = datetime.now()
time_stamp = datetime.timestamp(current_dt)
print(current_dt, " -> ", time_stamp)

# TimeStamp to DateTime
obj_dt = datetime.fromtimestamp(time_stamp)
print(time_stamp, " -> ", obj_dt)

# String to DataTime
str1 = "2021-01-01" # yy-mm-dd
dt1 = datetime.strptime(str1, "%Y-%m-%d")
print(type(str1))
print(type(dt1))
print(dt1)

# Date Difference
str1 = "2000-01-10" # yy-mm-dd
str2 = "2022-02-13" # yy-mm-dd
dt1 = datetime.strptime(str1, "%Y-%m-%d")
dt2 = datetime.strptime(str2, "%Y-%m-%d")
diff = dt2-dt1
print(diff)
print("Years: ", diff//365)

# Task-14.2
    # Time Difference
    # https://www.php.net/manual/en/function.date.php

# 14.2 Encryption
# Sending values from application to application
# Sending values from device to device
# We need to make secure our date
# data (original) -> Encrypt -> send -> Decrypt -> data (original)

# Pre-requirities
    # File (Create, Write, Read data from file)
    # Database (Create table, insert record, update record, and select record)

# Install Package
# python -m pip install cryptography

# Getting a Key
from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# print(key) # b'OoCdeH-FL-RZrNGcKt4LBpSQyZXKSU7yjfO0yJ8vmsY='

# Note:
    # Save in file
    # Save in database table

key_file = "key.txt"
# Save in file
# file = open("key.txt", 'wb')
# file.write(key)
# file.close()

# Read from file
file = open(key_file, "rb")
key = file.read() # System defined key
file.close()
# print(key)
# print(key.decode('utf-8'))

# Encrypting data
str1 = "Broadways InfoSys Nepal"
str2 = str1.encode()
print(str1)
print(str2)
f = Fernet(key)
str3 = f.encrypt(str2)
print(str3) # Encrypted Data

# Decrypting data
f= Fernet(key)
str4 = f.decrypt(str3)
print(str4)
print(str4.decode('utf-8'))

#Task-14-2.1
    # Encrypt file with contents
    # Decrypt encrypted file with contents

# Task-14-2.2
    # Encrypt and decrypt data using user defined key

"""
Note:
    - Sensitive data (password, pincode, email, date of birth, balance amount, atm passcode) - encrypt (database, file write)
    - key (file, or database), encrypt with key, decrypt with key
"""

# 14.3 Module, Package
# Module -> Python Program File (*.py) (Variables, Functions, Classes)
# Package -> Folder which contain modules (A folder must contain __init__.py file)

# from pkg1 import test # import
# print(test.var1)  # Access
# test.var1=45 # Update
# print(test.var1) # Access

# print(test.f1()) # Call function

# obj1 = test.C1()
# print(obj1.f2())

# 14.4 os Module (Operating System)
import os
# get current working folder
current_path = os.getcwd() # D:\Python\PythonDjango-4\CorePython-4\fundamentals

# create folder
# os.mkdir("folder1")
# os.makedirs("folder2\\folder3\\folder4")

# rename folder
# os.rename("folder1","folder12")

# delete folder
# os.remove("folder12")

import shutil
# copy file
# shutil.copyfile("1. hello.py", "2. hello.py")

# rename file
# os.rename("2. hello.py", "myfile.py")

# delete file
# os.remove("myfile.py")

# list all files/folders
allfiles = os.listdir()
print(len(allfiles))
for file in allfiles:
    print(current_path+"\\"+file)

# 14.5 sys Module
import sys
# exc_info()
# System Error Display
try:
    print("try...")
    print(20/0)
except:
    # print("Error: ", sys.exc_info()) # (<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x0000021414B65180>)
    print("Error: ", sys.exc_info()[1])  # (<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x0000021414B65180>)
finally:
    print("finally...")

# exit()
result = False
if(result):
    exit(0)
else:
    print("False")

# getsizeof()
var1 = 123456789101112131415
print(sys.getsizeof(var1))

# path
print(sys.path)

# version_info
print(sys.version_info)

# version
print(sys.version)

# 14.6 Jupyter NoteBook
# Python IDE (Integrated Development Environment)
# Installing Notebook
# https://jupyter.org/install
# pip install notebook

# Starting Notebook
# cmd -> jupyter notebook

# 14.7. JupyterLab
# https://jupyter.org/install
# pip install jupyterlab # Install
# jupyter-lab # Start

# 14.8 Spyder IDE
# pip install spyder # install
# pip install --upgrade spyder # Update/Upgrade

# 14.9 Others
    # PyCharm
    # Visual Studio Code