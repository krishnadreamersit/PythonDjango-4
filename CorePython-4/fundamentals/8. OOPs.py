# Structured Programming
    # varaible
    # function
    # separated | isolated

# Object Oriented Programming
    # varaible
    # function
    # combined form

# Class
    # Methods - functions
        # variables
        # input, process, output

# Object <- Class
# Object.method()

# Example-1
""" How to create a class? """
"""
class Person():
    pass
"""
""" How to create an object of Class? """
# person1 = Person()  # person1 is an object of Person Class
                    # person1 can access the resources of Person Class (variables, and methods)

# Example-2
"""
class Person():
    pid = 11
    name="Raj Thapa"
    address="Kahmandu, Nepal"

p1 = Person()
p2 = Person()
p3 = Person()

p1.pid=15

print(p1.pid, p1.name, p1.address)
print(p2.pid, p2.name, p2.address)
print(p3.pid, p3.name, p3.address)
"""

# Example-3
"""
class Person():
    def __init__(self):  # initializer function | constructor | magic function | self calling function while we create an object of respective class
        self.pid = 1
        self.name="Raj"
        self.address="KTM"
"""

# object declare and initialize
"""
p1 = Person() # __init__ function automatically call
p2 = Person() # __init__ function automatically call
p3 = Person() # __init__ function automatically call

print(p1.pid, p1.name, p1.address)
print(p2.pid, p2.name, p2.address)
print(p3.pid, p3.name, p3.address)

p1.pid=1
p1.name="John"
p1.address="KTM"

p2.pid=2
p2.name="Unanyan"
p2.address="BHK"

p3.pid=3
p3.name="Shree"
p1.address="LAT"

print(p1.pid, p1.name, p1.address)
print(p2.pid, p2.name, p2.address)
print(p3.pid, p3.name, p3.address)

# Example-4
class Person():
    # self -> Current Class
    def __init__(self, pid, name, address):
        self.pid=pid
        self.name=name
        self.address=address

    def __str__(self):
        return str(self.pid)+" "+self.name+" "+self.address

p1 = Person(1, "Amulya", "KTM") # () -> __init__() function
print(p1.pid, p1.name, p1.address)
print(p1) # __str__

# Example-5
class Person():
    def __init__(self, pid, name, address):
        self.pid=pid
        self.name=name
        self.address=address

    # getters and setters methods

    # getters
    def getPID(self):
        return self.pid

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    # setters
    def setPId(self, pid):
        self.pid=pid

    def setName(self, name):
        self.name=name

    def setAddress(self, address):
        self.address=address

    # to_string
    def __str__(self):
        return str(self.pid)+", "+self.name+", "+self.address

p1 = Person(1, "Raj Rai","KTM") # Magic function call i.e. __init__()
print(p1) # Magic function call i.e. __str__()
p1.setName("Rajan Thapa")
print(p1)
"""

# Task9_1
    # Create a class which can perform add, sub, mul, div, pow, sqrt.
    # Test in Console App
    # Test in Web app

# Task9_2
    # Create Student class and add features to calcualte total, average, result, and grade
    # Test in Console App
    # Test in Web app

# Example-6 [Default parameter]
"""
class Person():
    def __init__(self, pid=0, name="", address=""):
        self.pid=pid
        self.name=name
        self.address=address

    # getters and setters methods
    # getters
    def getPID(self):
        return self.pid

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    # setters
    def setPId(self, pid):
        self.pid=pid

    def setName(self, name):
        self.name=name

    def setAddress(self, address):
        self.address=address

    # to_string
    def __str__(self):
        return str(self.pid)+", "+self.name+", "+self.address

person1 = Person()  # def __init__(self, pid=0, name="", address=""):

person2 = Person(name="Raj", address="KTM")  # def __init__(self, pid=0, name="", address=""):
person2.setPId(2)

person1.setPId(1)
person1.setName("Kamal")
person1.setAddress("BHK")

print(person1) # All Values
print(person2) # All Values

print(person1.getName())
print(person2.getAddress())
"""

# OOPs
    # Class
        # Collection of varaibles and methods (function) - Encapsulation
            # Method Overloading
        # Inheriting resource of existing class - Inheritance
            # Method Overriding?


# Example-7
"""
class C1():
    def f1(self):
        print("Hello from f1")
    def f2(self):
        print("Hello from f2")

class C2(C1): # C2 is inherited from C1 class. C2 can consume the resources of C1 Class.
    pass

obj1 = C1()
obj2 = C2()

obj2.f1()
obj1.f2()
obj2.f2()
"""

# Task9_3
    # Explore the concept of Encapsulation, Method Overloading, Inheritance, and Method Overriding with proper example.

# Encapsulation
class Person():
    def __init__(self, pid=0, name=''):
        self.pid = pid
        self.name = name

    # getters
    def getPID(self):
        return self.pid

    def getName(self):
        return self.name

    # getters
    def setPID(self, pid):
        self.pid=pid

    def setName(self, name):
        self.name=name

    def __str__(self):
        return str(self.pid)+", "+self.name

# Encapsulation
    # Binding variables and methods in one class
    # pid, name - variables
    # __init__()
    # getPID()
    # getName()
    # setPID()
    # setName()
    # __str__()

# Method Overloading
# One method (function) have different forms in a single class
class Person():
    def __init__(self, pid=0, name=''):
        self.pid = pid
        self.name = name

# One function have four forms - method overloading
p1 = Person()
p2 = Person(pid=1)
p3 = Person(name='Unanayan')
p4 = Person(2, "John")


# Method Overriding
class Person():
    def __init__(self, pid=0, name=''):
        self.pid = pid
        self.name = name

    def getPID(self):
        return self.pid

class Student():
    def __init__(self, grade='', section=''):
        self.grade = grade
        self.section=section

class NewStudent(Person): # NewStudent is sub class of Person class
    def __init__(self, pid=0, name='', grade='', section=''):
        super.__init__(self, pid, name)  # super -> Super Class i.e. Person
        self.grade = grade
        self.section=section

    def getPID(self): # Method Overriding
        return super().getPID()

    # Super Class's method re-write in current class (child class) is called method overriding

s1 = NewStudent()
s1.pid=1
s1.name="John"
s1.grade="BSCIT"
s1.section="A"

