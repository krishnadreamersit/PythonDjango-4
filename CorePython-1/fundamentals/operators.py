# 1. print, input, types(bool, int, float, str), type conversion, type casting
# 2.1 Operators in Python
# 2.2 Operator Precedence and Associativity

# Operators in Python
# 1. Assignment Operator [ = ]
# 2. Arithmetic Operator [+, -, *, **, /, //, %, pow, sqrt]
# 3. Relational Operator [==, !=, >, >=, <, <=]
# 4. Logical Operator [and, or, not]

# 1. Assignment Operator [ = ]
# 1.a. Simple Assignment Operator [ = ]
"""
variable = value # value (right) assign to variable (left)
"""
# Example-1
var1 = True # Assignment (True assign to var1)
var2 = var1 # Assignment (value of var1 assign to var2)
print(var1, var2)

# Python Extra
var1, var2 = 78, 65
print(var1, var2)

# Python Extra
var1, var2 = var2, var1
print(var1, var2)

# 1.b. Multiple Assignment Operator [ = ... = .... = ..... ]
var1 = var2 = var3 = 100
print(var1, var2, var3)

# 1.c. Short-hand Assignment Operator [+=, -=, *=, /=, //=, %=]
var1 = 45
print(var1) # 45
var1 = var1 + 5 # increase var1 by 5
print(var1) # 50
var1 += 5 # var1 = var1 + 5
print(var1) # 55 # increase var1 by 5

# 2. Arithmetic Operator [+, -, *, **, /, //, %, pow, sqrt]
# 2.a. + [ADD]
# bool
print(True + True) # 2
print(True + False) # 1
print(False + False) # 0

print(True + 123)
print(True + 123.456)
# print(True + "Kathmandu") # TypeError: unsupported operand type(s) for +: 'bool' and 'str'

# int
print(34+32) # 66
print(12+False)
print(45+567.89)
# print(34+"Kathmandu") # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# float
print(34.56+89.76) # 124.32000000000001
print(123.456+12)
print(123.456+True)
# print(123.456+"Kathmandu") # TypeError: unsupported operand type(s) for +: 'float' and 'str'

# str
print("Kathmandu"+"Nepal") # KathmanduNepal
# print("Nepal"+True) # TypeError: can only concatenate str (not "bool") to str
# print("Nepal"+123) # TypeError: can only concatenate str (not "int") to str
# print("Nepal"+456.789) # TypeError: can only concatenate str (not "float") to str


# 2.b. - [SUB] - Numeric Type
print(10-5)
print(123.456-23.789)
print(6-34)


# 2.c. * [PRD] - Numeric Type
print(10*5)
print(123.456*23.789)
print(6*34)
print(6*3.5)

# Pyhton Extra
print("Broadway "*2)
print(2**3) # Power
import math
print(math.pow(2,3)) # 2 - base, 3 - exponent

# 2.d. / [Div] - Numeric Type
print(10/2)  # 5.0 (int/int-float)
print(10.23/5) # 2.0460000000000003 (float/int-float)
print(10/3) # 3.3333333333333335 (int/int-float)
print(10//3) # 3 (int//int-int)
print(10%3) # 1 (rem)

# Note : Calculate Square - root
import math
print(math.sqrt(16)) # 4.0 (int-float)

# 3. Relational Operator [==, !=, >, >=, <, <=]
# Compares two values and return boolean result (True/False)
#3.a. Equals to [ == ]
# if both values are equals than return True else return False
print(10==45) # False
print(10==10) # True
print(12==10) # False

#3.b. Not equals to [ != ]
# if both values are not equals than return True else return False
print(10==45) # True
print(10==10) # False
print(12==10) # True

#3.c. Greater than [ > ]
# if left values is greater than right value then return True else return False
print(10>5) # True
print(10>11) # False
print(11>11) # False

#3.d. Greater than or equals to [ >= ]
# if left values is greater than or equals with right value then return True else return False
print(10>=5) # True
print(10>=11) # False
print(11>=11) # False

#3.e. Less than [ < ]
# if left values is greater than right value then return True else return False
print(10<5) # False
print(10<11) # True
print(11<11) # False

#3.e. Less than or equals [ <= ]
# if left values is less than or equals to right value then return True else return False
print(10<=5) # False
print(10<=11) # True
print(11<=11) # True

# 4. Logical Operator [and, or, not]
# Compares two or more than two conditions and return single result.

# and, or
# (condition1) and (condition2)
# (condition1) or (condition2)
# (condition1) and (condition2) or (condition3)
print((10>=5) and (10>6)) # True
print((10>=5) and (10>60)) # False
print((10>=5) or (10>6)) # True
print((10>=5) or (10>60)) # True
print((10>=15) or (10>60)) # False

# not
print(not True) # False
print(not False) # True

# 5. Bitwise operators - Low-level (NA)

# 6. Other Operators
# [], {}, (), .

# 2.2 Operator Precedence and Associativity ?
print(10+3-7*6/2**3%3+5) # Processing order of operators
















