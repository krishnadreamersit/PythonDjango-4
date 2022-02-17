# Array
# Collection of similar type (int, unicode character, float)

# from array import array
# arr1 = array('i', [4,5,6,7,8,9])

# List [ ]
# Collection of values (any types and any number)

# Declare and Initialize
# list1 = list()
# print(list1)

# append(self, object, /)
# Append object to the end of the list.
"""
list1.append(True) # 0 index
list1.append(False) # 1 index
list1.append(1) # # 2 index
list1.append(25.58) # # 3 index
list1.append("Broadway") # 4 index
print(list1)
list1.append(arr1) # Add array # index 5
print(list1)
"""

# Indexing - Single Value (Positive and Negative Indexing)
# print(list1[5])
# print(list1[6]) # Individual element access # IndexError: list index out of range

# Slicing - Multiple values
# print(list1 [0:len(list1)]) # 0 to 5
# print(list1 [:len(list1)]) # 0 to 5
# print(list1 [0:]) # 0 to 5
# print(list1 [0:len(list1):1]) # 0 to 5
# print(list1 [0:len(list1):2]) # 0 to 5

# Declare and initialize
list1 = list() # Blank list

list1 = [4,5,7,8,9,3] # declare and initialize

from array import  array
arr1 = array('i', [6,7,8,9,2,3,4,5])
list1 = list(arr1) # declare and initialize list by array

# Basic functions
"""
import sys
print(list1)
print(type(list1))
print(id(list1))
print(isinstance(list1, list))
print(sys.getsizeof(list1))
print(len(list1))
print(max(list1))
print(min(list1))
print(sum(list1))
"""

# List with for loop
# list1 = [6, 7, 8, 9, 2, 3, 4, 5]

# Print all the values

# 1. index - individual
# print(list1[0], list1[1])

# 2. Slicing
# print(list1[:])

# 3. Looping Statement
# list1 = [6, 7, 8, 9, 2, 3, 4, 5]
# for item in list1:
#     print(item, end=' ')

# Explore list Class

# append(self, object, /)
# Append object to the end of the list.
"""
list1 = [6, 7, 8, 9, 2, 3, 4, 5]
print(list1)
list1.append(3)
print(list1)
"""

# clear(self, /)
# Remove all items from list.
# list1 = [6, 7, 8, 9, 2, 3, 4, 5]
# print(list1)
# list1.clear()
# print(list1)

# copy(self, /)
# Return a shallow copy of the list.
"""
list1 = [6, 7, 8, 9, 2, 3, 4, 5]
list2 = list1 # Copy by reference
print(list1)
print(list2)
# Memory address of list1 and list2
print(id(list1))
print(id(list2))

list3 = list2.copy() # Copy by value
print(id(list1))
print(id(list2))
print(id(list3))
"""

# count(self, value, /)
# Return number of occurrences of value.
"""
list1 = [6, 7, 3, 8, 9, 2, 3, 4, 5]
num1 = 3
count = list1.count(num1)
print(count)
"""

# extend(self, iterable, /)
# Extend list by appending elements from the iterable.
"""
list1 = [2,3,4,5,6]
list2 = [6,7,8,9]

from array import array
arr1 = array('i', [8,6,5,3,2])

print(list1)
list1.extend(list2)
print(list1)
list1.extend(arr1)
print(list1)
"""

# index(self, value, start=0, stop=9223372036854775807, /)
# Return first index of value.
"""
list1 = [2, 3, 4, 5, 6, 6, 7, 8, 9, 8, 6, 5, 3, 2]
num = 10
result = list1.index(num, 0, len(list1)-1) # ValueError: 10 is not in list
print(result)
"""

"""
list1 = [2, 3, 4, 5, 6, 6, 7, 8, 9, 8, 6, 5, 3, 2]
num = 10
count = list1.count(num)
if(count>0):
    result = list1.index(num, 0, len(list1)-1) # ValueError: 10 is not in list
    print(result)
else:
    print("Not found")
"""

# Dynamic
"""
list1 = [2, 3, 4, 5, 6, 6, 7, 8, 9, 8, 6, 5, 3, 2]
num = int(input("Enter number to search : "))
count = list1.count(num)
if(count>0):
    result = list1.index(num, 0, len(list1)-1) # ValueError: 10 is not in list
    print(result)
else:
    print("Not found")
"""

# insert(self, index, object, /)
# Insert object before index.
"""
list1 = [2, 3, 4, 5, 6, 6, 7, 8, 9, 8, 6, 5, 3, 2]
list1.insert(2, 99)
print(list1)
"""

# pop(self, index=-1, /)
# Remove and return item at index (default last).
"""
list1 = [2, 3, 4]
list1.pop()
print(list1)
list1.pop()
print(list1)
list1.pop()
print(list1)
"""

"""
list1.pop() # IndexError: pop from empty list
print(list1)
"""

# remove(self, value, /)
# Remove first occurrence of value.
"""
list1 = [2, 3, 4]
list1.remove(3) # Value to remove
print(list1)
list1.remove(10) # ValueError: list.remove(x): x not in list
print(list1)
"""

# reverse(self, /)
# Reverse *IN PLACE*.
"""
list1 = [2, 3, 4]
list1.reverse()
print(list1)
"""

# sort(self, /, *, key=None, reverse=False)
# Sort the list in ascending order and return None.
"""
list1 = [2, 3, 4, 5, 6, 6, 7, 8, 9, 8, 6, 5, 3, 2]
list1.sort(reverse=False) # ASC
print(list1)
list1.sort(reverse=True) # DESC
print(list1)
"""