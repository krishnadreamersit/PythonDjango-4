# Functions
"""
# Why function?
    # Write once use many

# What is function?
    Expression(s)?
    num1 = 10 [if valid python code] part1 (num1) part2 (=) part3 (10)
    part1 (num1)    part2 (=)       part3 (10)
    expression1     expression2     expression3

    Statement(s)?
    Collection of expressions to perform certain task is called Statement.

    num1 = 10 # Statement-1
    num2 = 8 # Statement-2
    num3 = num1 + num2 # Statement-3
    print(num3) # Statement-4

    Function(s)?
    Named (user defined name) satement(s) which perform certain task.

# How to create function?
    # defined a function named doSum():
    def doSum():
        num1 = 10 # Statement-1
        num2 = 8 # Statement-2
        num3 = num1 + num2 # Statement-3
        print(num3) # Statement-4

# How to use function?
    # call a function
    doSum()
"""

# Defined functions
def f1_1():
    print("Hello from f1_1")

def f1_2():
    print("PERSONAL INFO")
    print("ID : 1")
    print("NAME: RAJ")
    print("ADDRESS: KTM")
    print("EMAIL : raj@gmail.com")

def f2_1(message): # Parameter-1 - variable which receive value from argument - is called paramter
    print(message) # NameError: name 'message' is not defined

def f2_2(label, message):
    print(label, message)

def f3_1():
    return 1

import random
def f3_2():
    return random.randint(1, 100)

def f4_1(var1): # Paramter - accept value; return
    var1=var1+1
    return var1

def f4_2(num1, num2): # Paramter - accept value; return
    num3 = num1 +num2
    return num3

# Categories of function
# 1. No Parameter; No Return type
# 2. Parameter(s); No Return type
# 3. No Parameter(s); Return type
# 4. Parameter(s); Return type

# 5. Document String # Description about function

# function define
def f1_3(): # function signature (name of function, parameter(s))
    """ this is a function which demonstrate the use of doc string """  # doc string - documentation string
    print("Hello from f1_3()") # function body # processing and return value


# Variable Scope and Lifetime
num1 = 6 # global variable
def f1_4():
    num1 = 5 # Local varaible of function
    print("num1 = {}".format(num1))

# f1_4() # 5
# print(num1) # is not declared or num1 is not global variable; we cannt access num1
# print(num1) # 6

# Recursive function
"""
def f1_5():
    ......
    f1_5()
"""
"""
def f1_5():
    print("Hello")
    f1_5()

def f1_6(num1):
    if num1 == 1:
        return 1
    else:
        return num1 +  f1_6(num1 - 1)
"""

# print(f1_6(5))

# Default Parameter
"""
def f1_7(num1=0, num2=0):
    return num1 + num2
"""
# num3 = f1_7(4, 5)
# print(num3) # 9

# num3 = f1_7() # TypeError: f1_7() missing 2 required positional arguments: 'num1' and 'num2'
# print(num3)
"""
num3 = f1_7(70, 30)
print(num3)

num3 = f1_7(num1=7, num2=8)
print(num3)

num3 = f1_7(num2=78, num1=63)
print(num3)
"""

# Anonymous/Lambda Function/One line function
# Example-1
# obj1 = lambda str1:str1
# print(obj1("Raj"))
# print(obj1("Broadway"))

# Example-2
# calc = lambda x, y: x+y # parameter(s) : function body
# print(calc(7,6))

# Call functions
"""
# f1() # Call
# f1() # Call
# f1() # Call
# f1() # Call
# f1() # Call

for i in range(0, 10):
    f1_1()

f1_2()

str1 = "Broadway InfoSys"
f2_1(str1) # str1 Argument (value to send to function)
f2_1("John Bista")
f2_1("Unanyan Thapa")


f2_2("ID ", 1)
f2_2("NAME ", "Amulya")
f2_2("ADDRESS ", "KTM")
f2_2("EMAIL ", "amulya@gmail.com")

var1 = f3_1()
print(var1)

var1 = f3_2()
print(var1)


var1 = f4_1(5)
print(var1)

var2 = f4_2(56, 34)
print(var2)

# doc String
f1_3()
print(f1_3.__doc__)
f1_5() # RecursionError: maximum recursion depth exceeded while calling a Python object
"""