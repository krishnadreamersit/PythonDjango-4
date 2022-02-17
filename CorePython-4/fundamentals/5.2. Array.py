# Array is a collection of similar type of values (i.e. integer, unicode character, floating point)
# Step-1 Import Library
from array import array

# Step-2 Declare an object
# arr1 = array('i') # arr1 is an object of array class which can store signed integer
# Exploring object of an array
# print(arr1) # array('i')
# print(type(arr1)) # <class 'array.array'>
# print(isinstance(arr1, array))
# print(id(arr1)) # 1748679711760
# print(len(arr1)) # 0
# print(max(arr1)) # 0
# print(min(arr1)) # 0
# print(sum(arr1)) # 0

# append(self, v, /)
# Append new value v to the end of the array.
# arr1.append(9)
# arr1.append(5)
# arr1.append(2)
# arr1.append(7)
# arr1.append(6)
# print(arr1) # array('i', [9, 5, 2, 7, 6])
# print(max(arr1)) # 9
# print(min(arr1)) # 2
# print(sum(arr1)) # 29

# count(self, v, /)
# Return number of occurrences of v in the array.
# arr1 = array('i', [9, 5, 2, 7, 6, 5, 2, 7, 6, 2, 7, 6, 5, 2, 7, 6, 7, 6, 5, 2, 7, 6, 2, 7, 6, 5, 2, 7, 6,7, 6, 2, 7, 6, 5, 2, 7, 6, 7, 6, 5, 2, 7, 6, 2, 7, 6, 5, 2, 7, 6])
# num = 2
# result = arr1.count(num)
# print(result)

# extend(self, bb, /)
# Append items to the end of the array.
# nums = [5,6,7,8,9] # List - Collection of numbers
# arr1 = array('i', [3,5,6,7,8])
# print(arr1)
# arr1.extend(nums)
# print(arr1)
# arr2 = array('i', [9,4,3,4,2])
# arr2.extend(arr1)
# print(arr2)

# tobytes(self, /)
# frombytes(self, buffer, /)

# tofile(self, f, /)
# fromfile(self, f, n, /)

# tolist(self, /)
# fromlist(self, list, /)

# tounicode(self, /)
# fromunicode(self, ustr, /)

# index(self, v, start=0, stop=9223372036854775807, /)
# Return index of first occurrence of v in the array.
# arr1 = array('i', [3,5,6,5,8])
# num = 5
# count = arr1.count(5)
# print(count)
# result1 = arr1.index(num, 0, len(arr1)-1)
# result2 = arr1.index(num, result1+1, len(arr1)-1)
# print(result1)
# print(result2)


# insert(self, i, v, /)
# Insert a new item v into the array before position i.

# arr1 = array('i', [3,5,6,5,8])
# print(arr1)
# arr1.insert(3, 4) # in index 3 -> value 4
# print(arr1)

# pop(self, i=-1, /)
# Return the i-th element and delete it from the array.
# arr1 = array('i', [3,5,6,5,8])
# print(arr1)
# result = arr1.pop() # Remove last
# print(result)
# print(arr1)
# result = arr1.pop() # Remove last
# print(result)
# print(arr1)

# remove(self, v, /)
# Remove the first occurrence of v in the array.
# arr1 = array('i', [3,5,6,5,8,6])
# print(arr1)
# arr1.remove(6) # Value 6 (first 6)
# print(arr1)
# arr1.remove(6) # Value 6 (first 6)
# print(arr1)

# reverse(self, /)
# Reverse the order of the items in the array.
# arr1 = array('i', [3,5,6,5,8,6])
# print(arr1)
# arr1.reverse()
# print(arr1)

# itemsize
# the size, in bytes, of one array item

# typecode
# the typecode character used to create the array

# arr1 = array('i', [3,5,6,5,8,6])
# print(arr1.itemsize) # 4
# print(arr1.typecode) # i

arr1 = array('i', [3,5,6,5,8,6])
num = 5
result1 = arr1.index(num, 0, len(arr1)-1)
print(result1)
result2 = arr1.index(num, result1+1, len(arr1)-1)
print(result2)
