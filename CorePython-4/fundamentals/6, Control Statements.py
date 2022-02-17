# Control Statements
    # Selection Statement
    # Looping Statement
    # Branching Statement

# Selection Statements
# Data Types
    # bool
    # int
    # float
    # array
    # str
    # list
    # tuple
    # set
    # dict

# Operators
    # =, = ... =...., += (Assignment)
    # +, -, *, **, /, //, %, power, sqrt (Mathematical)
    # ==, !=, >, >=, <, <= (Comparision)
    # and, or , not (Logical)
    # Others (., [], {}, ()....)

# Condition
    # Value1 ComparisionOperator Value2 -> bool (Result)
    # 10 == 10 -> True
    # 10 != 11 -> True
    # 10 > 5 -> True
    # 10 >= 10 -> True
    # 10 < 10 -> False
    # 10 <= 10 -> True

# Selection Statements
# 1. if statement
# 2. match case (switch)

# 1. if statement
#a. if Statement
# Example-1
# num1 = 0
# if (num1 == 0):
#     print("Zero")

# Example-2
# num1 = 0
# if num1 == 0:
#     print("Zero")

#b. if else Statement
# Example-2
# num1 = 58
# if num1 == 0 :
#     print("Zero")
# else:
#     print("Non-zero")

# Example-3
# num1 = int(input("Enter any number : "))
# if num1 == 0 :
#     print("Zero")
# else:
#     print("Non-zero")

# if elif Statement
# Example-4
# num1 = int(input("Enter any number : "))
# if num1 == 0 :
#     print("Zero")
# elif num1==1:
#     print("One")
# elif num1==2:
#     print("Two")
# elif num1==3:
#     print("Three")
# elif num1==4:
#     print("Four")
# elif num1==5:
#     print("Five")
# else:
#     print("Out of range")

# How to check the balance of your cell phone
    # *400# Dial -> Text
    # 1415 Dial -> Sound (Number -> Text -> Speech)

# How to convert number to word?
    # 1 - One
    # 10 - Ten
    # 101 - One hundred and one
    # 1102 - One thousand one hundred and two

# How to convert number to speech?
    # Number -> Word -> Speech

# Nested if
# num1 = 9
# num2 = 6
# num3 = 5
# if num1 > num2:
#     if num1 > num3:
#         print(num1)
#
# if num2 > num1:
#     if num2 > num3:
#         print(num2)
#
# if num3 > num1:
#     if num3 > num2:
#         print(num3)

# if statement with multiple conditions (and , or)
# num1 = 9
# num2 = 6
# num3 = 5
# if num1 > num2 and num1 > num3:
#     print(num1)
#
# if num2 > num1 and num2 > num3:
#     print(num2)
#
# if num3 > num1 and num3 > num2:
#     print(num3)

# Not operator
# num1 = 0
# result =(num1 == 0)
# print(result) # True
# print(not result) # False (True-> False) (False-> True)

# 2. match case (switch)
# num1 = int(input("enter your number : "))
# match num1:
#     case 0:
#         print("Zero")
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case 3:
#         print("Three")
#     case 4:
#         print("Four")
#     case 5:
#         print("Five")
#     case _:
#         print("out of range")

# B. Looping Statement
# 1. while loop
# 2. for loop

# 1. while loop
"""
Syntax
    while(condition):
        statement(s)
"""
# Example -1. Print 1 to 5
"""
start = 1
stop = 5
while(start<=stop):
    print(start)
    start+=1
"""


# Example -2. Print N1 to N2
"""
start = int(input("enter first no : "))
stop = int(input("enter last no : "))
while(start<=stop):
    print(start)
    start+=1
"""

# Example -3. Print 5 to 1
"""
start = 5
stop = 1
while(start>=stop):
    print(start)
    start-=1
"""

# 2. for loop
"""
for(range):
    statement(s)
"""

# Example-1
"""
for i in range(0, 10): # 0 to less than 10 (i.e. 9)
    print(i+1)
"""

# Example-2
"""
for i in range(0, 10, 2): # step by 2
    print(i+1)
"""

# Example-3
"""
for i in range(10, 0, -1):
    print(i)
"""

# Nested Loop
# for i in range(0, 5): # outer loop
#     for j in range (6, 10): # inner loop
#         print(j)

#3. Branching Statement

# Break
"""
for i in range(0, 10):
    if i == 5:
        break # terminate loop - break
    print(i)
"""

# continue
"""
for i in range(0, 10):
    if i == 5:
        continue # escape the following lines to execute
    print(i)
"""

# pass
for i in range(0, 10):
    pass # No code

class Class1():
    pass

def f1():
    pass

# return
def f2():
    return "Hello"


