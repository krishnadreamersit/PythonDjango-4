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