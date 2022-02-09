# Error Handling (Exceptions)
# 1. Syntax Error
# 2. Runtime Error (Exception)
# 3. Logical Error (Mistake in Program)

# 1. Syntax Error
# print("hello) # SyntaxError: unterminated string literal (detected at line 7)
# print("hello") # Solution

# NameError
# print(x+y) # NameError: name 'x' is not defined # NameError: name 'y' is not defined
# x=8
# y=7
# print(x+y)

# SyntaxError: invalid syntax
# print(4***5)
# print(4**5)

# 2. Runtime Error

# Example-1
# num1 = int(input("enter first no : "))
# num2 = int(input("enter second no : "))
# num3 =  num1 + num2
# print("result : ", num3)

"""
enter first no : 10
enter second no : 25
result :  35
"""

# enter first no : 12.25 # ValueError: invalid literal for int() with base 10: '12.25'

# Example-2
# num1 = float(input("enter first no : "))
# num2 = float(input("enter second no : "))
# num3 =  num1 + num2
# print("result : ", num3)

# enter first no : 12.25
# enter second no : 10
# result :  22.25

# Example-3
# num1 = float(input("enter first no : "))
# num2 = float(input("enter second no : "))
# num3 =  num1 + num2
# print("result : ", num3)

# enter first no : 1O  # ValueError: could not convert string to float: '1O'

# Solution of ValueError: Data Validation
    # accept input from keyboard
    # check the validity (valid format) of value which accept from keyboard
    # if value is in valid format than
        # convert to specific type
    # else
        # alert to user for valid value to be entered

# Example-4
"""
tmp1 = input("Enter first no : ")
if tmp1.isdigit():
    num1 = int(tmp1)
    num1 +=1
    print(num1)
else:
    print("Please enter numeric value only")
"""

# Exception Handling
# Example-5
"""
num1 = 10
num2 = 0
num3 = num1/num2 # ZeroDivisionError: division by zero
print("Result : {}".format(num3))
"""

# Example-6
"""
import sys
num1 = 10
num2 = 0
num3 = 0

try:
    # input, process, output
    num3 = num1/num2 # ZeroDivisionError: division by zero
    print("Result : {}".format(num3))
except:
    # print("Error: ", sys.exc_info()) # Error Message
    print("Error : ", sys.exc_info()[1])  # Error Message
finally:
    del num1
    del num2
    del num3

# How to create user defined exceptions
class MyException(Exception):
    pass

class NumberTooSmallException(MyException):
    pass

class NumberTooLargeException(MyException):
    pass

import sys
num1 = 0
try:
    num1 = int(input("Enter any number : "))
    if(num1<0):
        raise NumberTooSmallException()
    elif(num1>10):
        raise NumberTooLargeException()
    else:
        print("Num : ", num1)
except NumberTooSmallException:
    print("Error : num1 is less than 0, please enter value between 0 - 10")
except NumberTooLargeException:
    print("Error : num1 is greater than 10, please enter value between 0 - 10")
except:
    print("Error : ", sys.exc_info()[1])
finally:
    del num1
"""

# 3. Logical Error - Debugging
# Debugging
# Tracing line by line execution of source code

# Example-1
# Library import
import sys

# Start and Declare # No Error - Syntax Error
num1 = None
num2 = None
num3 = None
try:
    # input, process, output
    num1 = int(input("Enter first no : ")) # Stop Point -> Debug (Shift + F9)
    num2 = int(input("Enter second no : "))
    num3 = num1 + num2
    print("Sum : ", num3)
except:
    # Error Message
    print("Error : ", sys.exc_info()[1])
finally:
    # Exit
    del num1
    del num2
    del num3




