# Declare & Initialize String
# str1 = 'Broadway Infosys'
# str2 = "Broadway Infosys"
# str3 = '''Broadway Infosys'''
# str4 = """Broadway Infosys"""

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
# str1=""
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

# encode(self, /, encoding='utf-8', errors='strict') ?
# Encode the string using the codec registered for encoding.

# endswith(...)
# S.endswith(suffix[, start[, end]]) -> bool
# Return True if S ends with the specified suffix, False otherwise.

# str1 = "suffix can also be a tuple of strings to try."
# result = str1.endswith(".")
# print(result)

# str1 = "suffix can also be a tuple of strings to try;"
# result = str1.endswith(";")
# print(result)

# expandtabs(self, /, tabsize=8)
# Return a copy where all tab characters are expanded using spaces.
# Tab -> Multiple Spaces

# str1 = "SN\tNAME\tADDRESS"
# str2 = "1\tKrishna\tKathmand"
# print(str1)
# print(str2)
# print(str1.expandtabs(20))
# print(str2.expandtabs(20))

# find(sub[, start[, end]]) -> int
# Return the lowest index in S where substring sub is found
# Return -1 on failure.

# str1 ="""Structural pattern matching has been added in the form of a match statement and case statements of patterns with associated actions. Patterns consist of sequences, mappings, primitive data types as well as class instances. Pattern matching enables programs to extract information from complex data types, branch on the structure of data, and apply specific actions based on different forms of data."""
# str2 ="patterns"
# result = str1.find(str2, 0, len(str1)-1)
# print(result)
#
# str2 ="Patterns"
# result = str1.find(str2, 0, len(str1)-1)
# print(result)

# str1 ="""Structural pattern matching has been added in the form of a match statement and case statements of patterns with associated actions. Patterns consist of sequences, mappings, primitive data types as well as class instances. Pattern matching enables programs to extract information from complex data types, branch on the structure of data, and apply specific actions based on different forms of data."""
# str2 ="the"
# count =str1.count(str2)
# print(count)  # times -> 2
# # position ?
# result1 = str1.find(str2, 0, len(str1)-1)
# print(result1)
# result2 = str1.find(str2, result1+len(str2), len(str1)-1)
# print(result2)

# str1 ="""Structural pattern matching has been added in the form of a match statement and case statements of patterns with associated actions. Patterns consist of sequences, mappings, primitive data types as well as class instances. Pattern matching enables programs to extract information from complex data types, branch on the structure of data, and apply specific actions based on different forms of data."""
# str2 ="of"
# count =str1.count(str2)
# print(count)
# result1 = str1.find(str2, 0, len(str1)-1) # 55
# result2 = str1.find(str2, result1+len(str2), len(str1)-1) # 96
# result3 = str1.find(str2, result2+len(str2), len(str1)-1) # 150
# result4 = str1.find(str2, result3+len(str2), len(str1)-1) # 329
# result5 = str1.find(str2, result4+len(str2), len(str1)-1) # 390
# print(result1, result2, result3, result4, result5)

# format(*args, **kwargs) -> str
# Return a formatted version of S, using substitutions from args and kwargs.

# firstname ="Unanyan"
# lastname ="Thapa"

# Fullnane : Unanyan Thapa # Expected Result
# print("Fullname : ", firstname, lastname)
# print("Fullname : {} {}".format(firstname, lastname))
# print("Fullname : {0} {1}".format(firstname, lastname))
# print("Fullname : {1} {0}".format(firstname, lastname))

# index(sub[, start[, end]]) -> int
# Return the lowest index in S where substring sub is found
# Raises ValueError when the substring is not found.

str1 = "Return the lowest index in S where substring sub is found. Raises ValueError when the substring is not found. Return True if the string is an alphabetic string, False otherwise."
str2 = "the"

# Solution-1
# count = str1.count(str2)
# print(count)
# result1 = str1.index(str2, 0, len(str1)-1)
# print(result1)
# result2 = str1.index(str2, result1+len(str2), len(str1)-1)
# print(result2)

# Solution-2
"""
file = open('D:\\Python\\PythonDjango-4\\resources\\Catching Fire.txt')
str1 = file.read()
str2 = "the"
count = str1.count(str2)
print("Total : {}".format(count))

if count>0:
    for i in range(count):
        if i ==0:
            result = str1.index(str2, 0, len(str1)-1)
            print("{} - {}".format(i, result))
        else:
            result = str1.index(str2, result+1, len(str1) - 1)
            print("{} - {}".format(i, result))
"""

# isalpha(self, /)
# Return True if the string is an alphabetic string, False otherwise.
# str1 = "ABC123"
# print(str1.isalnum()) # True
#
# str1 = "ABC 123"
# print(str1.isalnum()) # True

# isalnum(self, /)
# Return True if the string is an alpha-numeric string, False otherwise.

# str1 = "ABC123"
# print(str1.isalnum()) # True

# str1 = "ABC 123"
# print(str1.isalnum()) # False

# isascii(self, /)
# str1 = "ABC 123"
# print(str1.isascii()) # True

# print(ord('A')) # ASCII Code -> 65 (0-255)
# print(chr(65)) # ASCII Code -> A

# str1 = "आज कुन कुन प्रदेशमा छ त बर्षा को सम्भावना??"
# print(str1.isascii()) # False -> Unicode

# print(ord('त')) # ASCII Code -> 2340
# print(chr(2340)) # ASCII Code -> त

# isdecimal(self, /)
# isdigit(self, /)
# isidentifier(self, /)
# islower(self, /)
# isnumeric(self, /)
# isprintable(self, /)
# isspace(self, /)
# istitle(self, /)
# isupper(self, /)

# join(self, iterable, /)
# Concatenate any number of strings.

# items =['Concatenate', 'any', 'number', 'of', 'strings.'] # List
# print(items)
# print(' '.join(items))

# lower(self, /)
# Return a copy of the string converted to lowercase.

# str1 = "Return A Copy of The String Converted to Lowercase."
# print(str1)
# print(str1.lower())

# strip(self, chars=None, /)
# Return a copy of the string with leading and trailing whitespace removed.
"""
str1 = " Broadway "
print(len(str1))
print(str1)

str2 = str1.strip()
print(len(str2))
print(str2)
"""

# lstrip(self, chars=None, /)
# Return a copy of the string with leading whitespace removed.

# rstrip(self, chars=None, /)
# Return a copy of the string with trailing whitespace removed.

"""
find function in python
"""
str1 = """
Strings are useful for holding data that can be represented in text form. 
Some of the most-used operations on strings are to check their length, 
to build and concatenate them using the + and += string operators, checking 
for the existence or location of substrings with the indexOf() method, 
or extracting substrings with the substring() method.
"""
str2 = "the"

count = str1.count(str2)
print(count)

# str.find(sub[, start[, end]] )

# default value
# start = 0
# end = len(str)

if(count>0):
    start = 0
    for i in range(count):
        if(i == 0):
            result = str1.find(str2, start, len(str1))
        else:
            result = str1.find(str2, result+len(str2), len(str1))
        print(result)