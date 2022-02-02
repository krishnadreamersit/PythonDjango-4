# Set {} - Collections
# set() -> new empty set object
# set(iterable) -> new set object - array, list, tuple
# from array import array
#
# set1 = set()
# arr1 = array('i', [3,4,5,6,7,8])
# set1 = set(arr1) # array
# set1 = set([1,2,3,4,5,6,7,8,9]) # List
# set1 = set((1,2,3,4,5,6,7,8,9)) # Tuple
# set1 = {5,6,7,8,9,4,2,4,6,7,8,9}

# Exploring Set
# import sys
# print(set1)
# print(type(set1))
# print(isinstance(set1, list))
# print(isinstance(set1, tuple))
# print(isinstance(set1, set))
# print(id(set1))
# print(sys.getsizeof(set1))
# print(min(set1))
# print(max(set1))
# print(sum(set1))

# list1 = [5, 1,2,3,4,5,2,3,4]
# tuple1 = (5, 1,2,3,4,5,2,3,4)
# set1 = {5,1,2,3,4,5,2,3,4}  # Unique values only
# print(list1)
# print(tuple1)
# print(set1) # {1, 2, 3, 4, 5}

# indexing  # TypeError: 'set' object is not subscriptable
# print(set1[0]) # TypeError: 'set' object is not subscriptable
# print(set1[:]) # TypeError: 'set' object is not subscriptable

# Upate value
# set1[2]=7 # TypeError: 'set' object does not support item assignment

# Iterate-1
# for item in set1:
#     print(item)

# Iterate-2
# i=0
# for item in set1:
#     if(i==3):
#         print(item)
#     i+=1

# Note:
# Set (Read only) -> List -> List update -> Set (Read only)

# Exploring Set Class
# add(...)
# clear(...)
# copy(...)
# discard(...)
# isdisjoint(...)
# issubset(...)
# issuperset(...)
# pop(...)
# remove(...)

# Set Operations

# Union
# set1 = {1,2,3,4,5}
# set2 = {3,4,5,6,7}
# set3 = set1.union(set2)
# print(set3)
# set3 = (set1 | set2)
# print(set3)

# Intersection
# set1 = {1,2,3,4,5}
# set2 = {3,4,5,6,7}
# set3 = set1.intersection(set2)
# print(set3)
# set3 = (set1 & set2)
# print(set3)

# Difference
# set1 = {1,2,3,4,5}
# set2 = {3,4,5,6,7}
# set3 = set1.difference(set2)
# print(set3)
# set3 = set2.difference(set1)
# print(set3)