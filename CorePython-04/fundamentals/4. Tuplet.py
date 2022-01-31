# Typles ( )
# Typle -> Collections (any type, any numbers, read-only)

tup1 = ()
print(type(tup1)) # <class 'tuple'>

tup1 = (3,4,5,6,7,8,9,10)
print(type(tup1)) # <class 'tuple'>

list1 = [7,8,9,0,10, 2]
tup1 = tuple(list1)
print(tup1)

from array import  array
arr1 = array('i', [8,3,4,3,4,3,2])
tup1 = tuple(arr1)
print(tup1)

# Explore tuple class

# count(self, value, /)
# Return number of occurrences of value.

# print(tup1.count(3))

# index(self, value, start=0, stop=9223372036854775807, /)
# Return first index of value.

# print(tup1.index(3, 0, len(tup1)-1))


