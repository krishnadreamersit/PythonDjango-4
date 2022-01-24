# Declare & Initialize String
str1 = 'Broadway Infosys'
str2 = "Broadway Infosys"
str3 = '''Broadway Infosys'''
str4 = """Broadway Infosys"""

# Access String
"""
print(str1)
print(str2)
print(str3)
print(str4)
"""

# Explore String
"""
str1 = 'Broadway'
print(len(str1)) # 8
"""

"""B    r   o   a   d   w   a   y"""    # Values
"""0    1   2   3   4   5   6   7"""    # Indexes (positive)
"""-8  -7  -6  -5  -4  -3  -2  -1"""    # Indexes (negative) # Python Extra

# Accessing Individual Character of String  # out of range -> IndexError
# print(str1[-9]) # IndexError: string index out of range
# print(str1[8]) # IndexError: string index out of range

# within range -> individual character
"""
print(str1[7]) # y
print(str1[-8]) # B
"""

# import sys
# print(sys.getsizeof('o'))

# print(dir(str))
# print(help(str))

#1. Decalre and Initialize
"""
str1 = "Broadway"
print(len(str1)) # 8
"""

#2. Indexing (+ve (0 to 7), -ve (-1 to -8)
# Extracting individual character from string
"""
print(str1[0])
print(str1[7])
print(str1[1])
print(str1[6])
"""

#3. Slicing
"""
str1 = "Broadway"
var1 = str1[0] # indexing - Extract individual character from string
print(type(var1)) # <class 'str'>
"""

"""
var2 = str1[0:7] # Slicing - Extract from 0 to less than 7 (i.e. 6) index
print(type(var2)) # <class 'str'>
print()
print(var1)
print(var2)
print()
"""

# Slicing
str1 = "Broadway" # Length 8
"""
print(str1[:]) # All
print(str1[0:5]) # 0 - 4
print(str1[3:7]) # 3 - 6
print(str1[0:])  # 0 - last
print(str1[:8])  # 0 - last
print(str1[::2]) # Skip by 2 # Broadway -> Boda
print(str1[::1]) # Skip by 2 # Broadway
"""

# print(str1[9]) # Indexing # IndexError: string index out of range ; must be < 8
# print(str1[:9]) # Slicing # No IndexError

# print(str1[0:8:1]) # [start: stop: step] till last stop # Broadway
# [0: 8: 2] [0, 2, 4, 6, 8]
# print(str1 [0:8:3]) # Baa

# Common functions
"""
import sys
str1 = "Broadway"
print(str1)
print(type(str1))
print(isinstance(str1, str))
print(isinstance(str1, int))
print(isinstance(str1, float))
print(isinstance(str1, bool))
print(id(str1))
print(len(str1))
print(max(str1))
print(min(str1))
print(sys.getsizeof(str1))
print(sys.getsizeof(str1[0]))
"""

# Exploring str class
# print(help(str))

# Declarign an object of str class
# Style -1
# str1 = str() # str1 is an object of str class
# print(type(str1)) # <class 'str'>
# print(len(str1))

# __add__(self, value, /)
"""
str1.__add__("What is Python?")
str1.__add__(" Executive Summary")
print(str1)
"""

# str1+="What is Python?"
# str1+=" Executive Summary"
# print(str1)

# Style -2
# str2 ="Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed."
# print(type(str2)) # <class 'str'>
# print(len(str2))

# str3 = "return a Capitalized Version of the String."

# capitalize(self, /)
# Return a capitalized version of the string.

# tmpstr = str3.capitalize()
# print(tmpstr) # Return a capitalized version of the string.

# tmpstr = str2.capitalize()
# print(tmpstr)

# casefold(self, /)
# Return a version of the string suitable for caseless comparisons.

# Example-1
"""
var1 ="admin"
var2 ="AdMin"
print(var1, var2) # admin AdMin
result1 = (var1 == var2)
print(result1)
"""

# Example-2
"""
var3 = var1.casefold()
var4 = var2.casefold()
print(var3, var4) # admin admin
result2 = (var3 == var4)
print(result2)
"""

# center(self, width, fillchar=' ', /)
# Return a centered string of length width.
"""
str1 = "Broadways"
str2 = str1.center(20, ' ')
print(str2) # ******Broadway******
"""

# ljust(self, width, fillchar=' ', /)
# Return a left-justified string of length width.
"""
str1 = "Broadways"
str2 = str1.ljust(20, '*')
print(str2) # Broadways***********
"""

# rjust(self, width, fillchar=' ', /)
# Return a right-justified string of length width.
"""
str1 = "Broadways"
str2 = str1.rjust(20, '*')
print(str2) #***********Broadways
"""

# S.count(sub[, start[, end]]) -> int
# Return the number of non-overlapping occurrences of substring sub in string
# str1 = """Return the number of non-overlapping occurrences of substring sub in string"""
# str2 = 'e'
# result = str1.count(str2)
# print(result) # 6

# str2 = 'the'
# result = str1.count(str2)
# print(result) # 6

# str2 = 'string'
# result = str1.count(str2)
# print(result)  # 2

# encode(self, /, encoding='utf-8', errors='strict')
# Encode the string using the codec registered for encoding.

# endswith(...)
# S.endswith(suffix[, start[, end]]) -> bool
# Return True if S ends with the specified suffix, False otherwise.

str1 = "suffix can also be a tuple of strings to try."
result = str1.endswith(".")
print(result)

str1 = "suffix can also be a tuple of strings to try;"
result = str1.endswith(";")
print(result)