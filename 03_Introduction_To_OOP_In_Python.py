# ------------------------------------------
# Scope in Python: Local vs Global
# ------------------------------------------

# Global scope: Defined outside any function
a = 15

def num():
    # Local variable: exists only inside the function
    a = 30
    print(a)  # Outputs 30 — Local scope

print(a)  # Outputs 15 — Global scope remains unchanged
num()
print(a)  # Still outputs 15 — Global 'a' not affected by local 'a'

# ------------------------------------------
# Using `global` Keyword (Not Recommended)
# ------------------------------------------

# global keyword allows a function to modify global variables

a = 15

def num():
    global a
    a = 30  # This changes the global 'a'
    print(a)  # Outputs 30

print(a)  #  15 (before function call)
num()     #  30 (modifies global a)
print(a)  #  30 (after function call — global 'a' changed)

# Avoid using global variables as they lead to unpredictable behavior
# Always prefer passing variables as function arguments.

# ------------------------------------------
# Object-Oriented Programming in Python
# ------------------------------------------

# What is OOP?
# OOP is a way to structure your code using classes and objects.
# It helps manage complexity in large codebases.

# Key Features of OOP:
# - Encapsulation
# - Abstraction
# - Inheritance
# - Polymorphism


# ------------------------------------------
# Classes vs Dictionaries
# ------------------------------------------

# Without classes: Using dictionaries to store student info
{
    33: {"name": "yasir", "age": 24},
    34: {"name": "ali", "age": 22},
    35: {"name": "ahmed", "age": 23}
}
#  Problem: Not scalable, error-prone, lacks structure

#  Solution: Use classes to model real-world entities


# ------------------------------------------
# Creating a Class
# ------------------------------------------

class Student:
    # Method to display student info
    def info(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")

    # Method to set student info using input
    def set_info(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.gender = input("Enter your gender: ")

# Creating objects (instances)
s1 = Student()
s2 = Student()

# Setting attributes for each object
s1.set_info()
s2.set_info()

# Displaying attributes
s1.info()
s2.info()


# ------------------------------------------
#  Common Error Example:
# ------------------------------------------

#  Accessing info before calling set_info will raise AttributeError
class Student:
    def set_info(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.gender = input("Enter your gender: ")

    def info(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")

s1 = Student()
# s1.info()   Throws AttributeError: 'Student' object has no attribute 'name'
s1.set_info()  # Set the attributes first
s1.info()      # Safe to access now


# ------------------------------------------
# Better Approach: Use __init__() Constructor
# ------------------------------------------

# __init__() is called automatically when an object is created.
# It helps initialize values during object creation.

class Student:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.gender = input("Enter your gender: ")

    def info(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")

# Now no need to call set_info separately
s1 = Student()
s1.info()

s2 = Student()
s2.info()

# ------------------------------------------
#  Summary:
# ------------------------------------------
#  Local Scope: Only exists inside a function
#  Global Scope: Available throughout the program
#  Avoid `global` keyword for better practice
#  Classes provide a clean, reusable structure
#  Use __init__() to avoid attribute initialization errors
#  Don’t access attributes before setting them!
# This file demonstrates foundational concepts in Python OOP and scope management.

