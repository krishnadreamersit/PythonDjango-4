# Declare & Initialize String
str1 = 'Broadway Infosys'
str2 = "Broadway Infosys"
str3 = '''Broadway Infosys'''
str4 = """Broadway Infosys"""

# Access String
print(str1)
print(str2)
print(str3)
print(str4)

# Explore String
str1 = 'Broadway'
print(len(str1)) # 8
"""B    r   o   a   d   w   a   y"""    # Values
"""0    1   2   3   4   5   6   7"""    # Indexes (positive)
"""-8  -7  -6  -5  -4  -3  -2  -1"""    # Indexes (negative) # Python Extra

# Accessing Individual Character of String  # out of range -> IndexError
# print(str1[-9]) # IndexError: string index out of range
# print(str1[8]) # IndexError: string index out of range

# within range -> individual character
print(str1[7]) # y
print(str1[-8]) # B

# import sys
# print(sys.getsizeof('o'))

# print(dir(str))
print(help(str))
