# What is Hierarchical Inheritance in Python?
# Hierarchical Inheritance occurs when multiple child classes inherit from a single parent class.


# syntax

class Parent:
    # Base class
    pass

class Child1(Parent):
    # Inherits from Parent
    pass

class Child2(Parent):
    # Inherits from Parent
    pass


# example
class Animal:
    def speak(self):
        print("Animals can speak")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


class Cat(Animal):
    def meow(self):
        print("Cat meows")


# Create objects of each child class
d = Dog()
c = Cat()

d.speak()  # From Animal
d.bark()   # Dog's own method

c.speak()  # From Animal
c.meow()   # Cat's own method

