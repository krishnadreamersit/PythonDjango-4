# Error Handling (Exceptions)
# 1. Syntax Error
# 2. Runtime Error
# 3. Logical Error

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
import sys

num1 = 10
num2 = 0
num3 = 0
try:
    num3 = num1/num2 # ZeroDivisionError: division by zero
    print("Result : {}".format(num3))
except:
    # print("Error: ", sys.exc_info()) # Error Message
    print("Error : ", sys.exc_info()[1])  # Error Message
finally:
    del num1
    del num2
    del num3

# 3. Logical Error
