# Extended Data Types
    # str
    # array
    # list
    # tuple
    # set
    # dictionary

#1. str (String)
# Representation
    # 'ABC'
    # "ABC"
    # '''ABC'''
    # """ABC"""

# Decalre
str1 = 'ABC'
str2 = "ABC"
str3 = '''ABC'''
str4 = """ABC"""
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))

str1 = "Broadway Infosys Nepal is one of the best inclusive computer training institutes in Kathmandu, Nepal. Established in 2008, our professional IT Training and Development center has been employing experts in this field to impart professional education."
print(str1)
print(type(str1))
print(id(str1))
print(isinstance(str1, str))
print(len(str1)) # 249
print(max(str1)) # Based on ASCII Value
print(min(str1)) # Based on ASCII Value

# A-Z a-z 0-9 Symbols (Character Set)
# Each character have it unique number called ASCII Code

# Documentation of module/class
# print(help(str))
# print(dir(str))
