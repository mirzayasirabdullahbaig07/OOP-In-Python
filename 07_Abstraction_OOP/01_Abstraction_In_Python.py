# -------------------------------
# Abstraction in Python (with example)
# -------------------------------

# What is Abstraction?
# Abstraction is a concept in object-oriented programming (OOP) 
# where we hide complex implementation details and show only the essential features to the user.
# It helps in reducing complexity and increases code reusability and readability.

# Real-life Example:
# Think of a car. You can drive it without knowing how the engine works.
# The internal complexity is hidden — you only interact with the car's interface (steering, brakes, accelerator).

# In Python, abstraction is achieved using:
# 1. Abstract Base Class (ABC)
# 2. @abstractmethod decorator

# Importing required modules from 'abc' (Abstract Base Classes)
from abc import ABC, abstractmethod

# Creating an abstract class 'Car' which acts as a blueprint for other classes
class Car(ABC):  # Inheriting from ABC to make it an abstract class
    
    # This is an abstract method — it has no body
    # Subclasses inheriting Car MUST override this method
    @abstractmethod
    def sound(self):
        pass

# Creating a subclass 'Audi' that inherits from 'Car'
class Audi(Car):
    
    # Constructor method to initialize engine details
    def __init__(self, engine) -> None:
        self.engine = engine  # Storing engine info in instance variable
    
    # Implementing the abstract method 'sound'
    def sound(self):
        print("SPORTS SOUND")

# Creating an object of Audi and calling the sound method
obj = Audi("1200cc")
obj.sound()

# -------------------------------
# Output: SPORTS SOUND
# -------------------------------

# Why use abstraction?
# - To define a common interface (structure) for all subclasses
# - To enforce certain methods in child classes
# - To hide internal details and show only necessary parts

# Important Points
# - Abstract classes cannot be instantiated directly.
# - Every abstract method must be implemented in child class.
# - If a class has even one abstract method, it becomes an abstract class.
