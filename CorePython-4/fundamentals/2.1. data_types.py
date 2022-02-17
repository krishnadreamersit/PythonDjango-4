# Data Types
    # bool
    # int
    # float
    # str

#1. bool - Boolean (True/False)
"""
On/Off
True/False
1/0
Yes/No
"""
import sys

"""
print(True)
print(False)
print(True) # Copy paste # Rashmi # Looping - John # Store in variable - Jeena # Loop - Amulya
"""

# result re-use
# steps
    # decalre variable
    # assign value
    # access value of varaible (at required line)
"""

var1 = True # decalre variable   # assign value
print(var1)  # access value of variable
print(var1)
print(var1)
print(var1)
print(var1)
"""

# type()
"""
var1 = True #True # False # decalre and assign
print(type(var1)) # type() return the type of value of variable
var1 = False # Re-decalre and assign
print(type(var1))
"""

# id() # return the memory location of varaible
"""
var1 = True # Declare and Assign
print(type(var1)) # Type of value in var1 # <class 'bool'>
print(id(var1)) # Memory Address # 140708264725352
print(var1) # Accessing the value of variable # True

var1 = False # Re-declare & assign
print(type(var1))
print(id(var1))
print(var1)
"""

# memory space - occupied by variable
# getsizeof()
"""
import sys
var1 = True
print(sys.getsizeof(var1)) # 28
"""

# all in one
"""
var1 = True # decalre and assign
print(var1) # accessing value
print(type(var1)) # type of value
print(id(var1)) # memory address of varaible
print(sys.getsizeof(var1)) # memory occupied by varaible
var1 = False # re-decalre and assign # Python Extra
print()
"""
# Python Extra
"""
var1 = True
var2 = True
print(var1, var2) # value
print(type(var1), type(var2)) # type
print(id(var1), id(var2)) # memory address
print(sys.getsizeof(var1), sys.getsizeof(var2)) # memory occupied
"""

# 2. int - Integer Number
    # Numeric Type - Whole number (without fractional values)
    # Add, Sub, Prd, Div, Pow, SQRT - Operations
    # ==, !=, >, >=, <, <= - Operations

"""
num1 = 123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789 # decalre and assign
print(num1) # access value
print(type(num1)) # type of value
print(id(num1)) # memory address
print(sys.getsizeof(num1)) # memory size (variable length)
"""

# Type Conversion
# str -> int
# float -> int
# bool -> int

# str -> int

# Example-1
"""
var1 = "123"
var2 = int(var1) # Type Conversion
print(type(var1)) # <class 'str'>
print(type(var2)) # <class 'int'>
"""

# Example-2
"""
var1 = "123.456"
# if value of var1 can convert to int or not? -> validation (value validation)
var2 = int(var1) # Type Conversion # ValueError: invalid literal for int() with base 10: '123.456'
print(type(var1)) # <class 'str'>
print(type(var2)) # <class 'int'>
"""

# basic validation
    # isinstance()

# Example-1
"""
var1 = 123
print(isinstance(var1, bool)) # False
print(isinstance(var1, int)) # True
print(isinstance(var1, float)) # False
print(isinstance(var1, str)) # False
"""

# Example-2
"""
var1 = "123"
print(isinstance(var1, bool)) # False
print(isinstance(var1, int)) # True
print(isinstance(var1, float)) # False
print(isinstance(var1, str)) # False
"""

# Example-3
"""
var1 = True
print(isinstance(var1, bool)) # False
print(isinstance(var1, int)) # True
print(isinstance(var1, float)) # False
print(isinstance(var1, str)) # False
"""

# Example2-1
"""
var1 = 123
print(isinstance(var1, bool)) # False
print(isinstance(var1, int)) # True
print(isinstance(var1, float)) # False
print(isinstance(var1, str)) # False
"""

# Example3-2
var1 = 123.456
var2 = 456.789
print(var1+var2)
print(var1-var2)
print(var1*var2)
print(var1/var2)

# Example3-3
var1 = 123.456
var2 = 456.789
print(var1==var2)
print(var1!=var2)
print(var1>var2)
print(var1>=var2)
print(var1<var2)
print(var1<=var2)

# 3. float - number with fractional values
    # add, sub, prd, div, power, sqrt
    # ==, !=, >, >=, <, <=

# Example3-1
"""
var1 = 123.456789
print(var1)
print(type(var1))
print(id(var1))
print(sys.getsizeof(var1))
print(isinstance(var1, float))
print(isinstance(var1, bool))
print(isinstance(var1, int))
print(isinstance(var1, str))
"""

# Example3-2
var1 = 123.456
var2 = 456.789
print(var1+var2)
print(var1-var2)
print(var1*var2)
print(var1/var2)

# Example3-3
var1 = 123.456
var2 = 456.789
print(var1==var2)
print(var1!=var2)
print(var1>var2)
print(var1>=var2)
print(var1<var2)
print(var1<=var2)

# 4. str - String  '', "", ''' ''', """ """ (any character)
# Example4-1
"""
var1 = 'ABC'
print(var1)
print(type(var1))
print(id(var1))
print(sys.getsizeof(var1))
print(isinstance(var1, float))
print(isinstance(var1, bool))
print(isinstance(var1, int))
print(isinstance(var1, str))
"""

# String operations
# add, sub, prd, div, pow, sqrt
var1 = "Kathmandu"
var2 = " "
var3 = "Nepal"
# print(var1+var2+var3) # Applicable
# print(var1-var2) # TypeError: unsupported operand type(s) for -: 'str' and 'str'
# print(var1*var2) # TypeError: can't multiply sequence by non-int of type 'str'
# print(var1/var2) # TypeError: unsupported operand type(s) for /: 'str' and 'str'
# print(var1 * 3) # KathmanduKathmanduKathmandu # Applicable

# ==, !=, >, >=, <, <= # Applicable (ASCII Code)
"""
var1 = "Kathmandu"
var2 = "kathmandu"
print(var1 == var2)
print(var1 != var2)
print(var1 > var2)
print(var1 >= var2)
print(var1 < var2)
print(var1 <= var2)
"""

# Basic Data Types
    # bool  - Boolean (True/False)
    # int - Whole number
    # float - Decimal number
    # str - String

# Type Conversion (string to other)
    # String to bool, int, float

# Type Casting (numeric to numeric)
    # int to float
    # float to int

"""
var1 = False # var1 = True
print(type(var1))  # <class 'bool'>
"""

"""
var1 = 123
print(type(var1))  # <class 'int'>
"""

"""
var1 = 123.456
print(type(var1))  # <class 'float'>
"""

# Type Conversion

# var1 = "Broadway InfoSys"
# var1 = 'Broadway InfoSys'
# var1 = """Broadway InfoSys"""
# var1 = '''Broadway InfoSys'''
# print(type(var1))  # <class 'str'>

# Type Conversion-1
#  int <- str
#  float <- str
#  bool <- str

# str -> int
var1 = "123" # str
var2 = int(var1) # str -> int
print(type(var2)) # int

# str -> float
var1 = "123.456" # str
var2 = float(var1) # str -> float
print(type(var2)) # float

# str -> bool
var1 = "True" # str
var2 = bool(var1) # str -> bool
print(type(var2)) # bool

# Others to String
var1 = True # False # 123 # 123.456
var2 = str(var1)
print(type(var2))

# Type Casting - 1 (int -> float, float-> int)
    # int to float
    # float to int

# int to float
var1  = 123
var2 = float (var1)
print(type(var2))

# float to int
var1  = 123.456
var2 = int (var1)
print(type(var2))