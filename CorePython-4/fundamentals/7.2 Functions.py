# Recursive function
# Function calling itself

import sys
sys.setrecursionlimit(100000)

# print("Hello")
def f1():
    print("Hello")
    f1() # RecursionError: maximum recursion depth exceeded while calling a Python object

# f1()

# Task
# Write recursive function which print 1 to 10 (N)
# Write recursive function which find specific word in sentence.
"""
As other answer has already give you a much nicer way for how to 
solve this in your case (which is to replace recursion by simple loop) 
there is another solution if you still want to use recursion which is 
to use one of the many recipes of implementing TRE in python like this one.
"""

"""
is
"""



