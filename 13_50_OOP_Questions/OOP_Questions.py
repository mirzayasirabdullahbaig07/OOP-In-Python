"""
OOP Practice Questions with Full Statements & Solutions
-------------------------------------------------------
Sections:
A. Classes & Objects (15 Questions)
B. Constructors & Destructors (10 Questions)
C. Inheritance (10 Questions)
D. Polymorphism & Encapsulation (10 Questions)
E. Advanced OOP (5 Questions)
"""

# ====================================================
# A. Classes & Objects (15 Questions)
# ====================================================

# 1. Create a Car class with attributes and a method to display car details.
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

# 2. Create a class Student with a method to calculate average marks.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

# 3. Implement a class Circle with methods to calculate area and perimeter.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# 4. Write a class Book that stores book title, author, and price.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

# 5. Create a class BankAccount with deposit and withdraw methods.
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")
        return self.balance

# 6. Implement a class Calculator with methods for basic operations.
class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): return a / b if b != 0 else "Error: Division by zero"

# 7. Create a class Rectangle with methods to find area and perimeter.
class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self): return self.l * self.w
    def perimeter(self): return 2 * (self.l + self.w)

# 8. Create a class Employee with a method to calculate annual salary.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

# 9. Write a class that counts the number of objects created.
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

# 10. Create a class that takes user input and stores it as attributes.
class UserInput:
    def __init__(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))

# 11. Make a class that checks if a number is prime.
class Prime:
    def __init__(self, num):
        self.num = num

    def is_prime(self):
        if self.num < 2: return False
        for i in range(2, int(self.num ** 0.5) + 1):
            if self.num % i == 0:
                return False
        return True

# 12. Create a class Time to display time in hours and minutes.
class Time:
    def __init__(self, h, m):
        self.h = h
        self.m = m

    def display(self):
        print(f"{self.h:02d}:{self.m:02d}")

# 13. Write a class to convert temperature between Celsius and Fahrenheit.
class Temperature:
    def to_fahrenheit(self, c):
        return (c * 9/5) + 32

    def to_celsius(self, f):
        return (f - 32) * 5/9

# 14. Make a class with a method that checks if a string is a palindrome.
class Palindrome:
    def __init__(self, text):
        self.text = text

    def check(self):
        return self.text == self.text[::-1]

# 15. Create a class Person with a method to introduce themselves.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I am {self.name}, {self.age} years old.")

# ====================================================
# B. Constructors & Destructors (10 Questions)
# ====================================================

# 16. Create a constructor to initialize values in a Laptop class.
class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

# 17. Write a class Point that initializes x and y coordinates.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 18. Demonstrate the use of a destructor using a print statement.
class Demo:
    def __init__(self):
        print("Object Created")
    def __del__(self):
        print("Object Destroyed")

# 19. Create a class that accepts name and age as parameters.
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 20. Write a constructor that sets default values if none are provided.
class DefaultExample:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

# 21. Demonstrate constructor overloading using default arguments.
class OverloadExample:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

# 22. Create a class with a constructor that logs object creation.
class Logger:
    def __init__(self):
        print("Object Created!")

# 23. Make a class that sets up a database connection on init and closes it on delete.
class Database:
    def __init__(self):
        print("DB Connection Opened")

    def __del__(self):
        print("DB Connection Closed")

# 24. Demonstrate multiple objects calling the same constructor.
obj1 = Logger()
obj2 = Logger()

# 25. Use constructor to validate inputs (e.g., raise error if age < 0).
class ValidateAge:
    def __init__(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.age = age

# ====================================================
# C. Inheritance (10 Questions)
# ====================================================

# 26. Create a base class Animal and a derived class Dog.
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# 27. Create a Vehicle base class and two child classes: Car and Bike.
class Vehicle:
    def move(self):
        print("Vehicle moves")

class CarVehicle(Vehicle):
    def move(self):
        print("Car drives")

class Bike(Vehicle):
    def move(self):
        print("Bike rides")

# 28. Use super() to access the parent class method in a child class.
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

# 29. Create a Shape class and inherit Circle and Rectangle from it.
class Shape:
    def area(self):
        pass

class CircleShape(Shape):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r ** 2

class RectangleShape(Shape):
    def __init__(self, l, w): self.l, self.w = l, w
    def area(self): return self.l * self.w

# 30. Implement multilevel inheritance with Person → Employee → Manager.
class PersonBase:
    def __init__(self, name): self.name = name

class EmployeeBase(PersonBase):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

class Manager(EmployeeBase):
    def __init__(self, name, salary, dept):
        super().__init__(name, salary)
        self.dept = dept

# 31. Create a base class with protected members accessed by child class.
class Base:
    def __init__(self):
        self._protected = "Protected Value"

class ChildBase(Base):
    def show(self):
        print(self._protected)

# 32. Demonstrate method overriding in inheritance.
class Bird:
    def sound(self): print("Some sound")

class Sparrow(Bird):
    def sound(self): print("Chirp Chirp")

# 33. Call a parent class method from a child class.
class ParentMethod:
    def show(self): print("Parent show")

class ChildMethod(ParentMethod):
    def show(self):
        ParentMethod.show(self)
        print("Child show")

# 34. Create a base class Appliance with a method, and override it in child.
class Appliance:
    def work(self): print("General Appliance")

class WashingMachine(Appliance):
    def work(self): print("Washing Clothes")

# 35. Implement hierarchical inheritance with a common parent.
class AnimalBase:
    def speak(self): print("Animal sound")

class DogH(AnimalBase):
    def speak(self): print("Bark")

class CatH(AnimalBase):
    def speak(self): print("Meow")

# ====================================================
# D. Polymorphism & Encapsulation (10 Questions)
# ====================================================

# 36. Demonstrate polymorphism using method overriding.
class ShapePoly:
    def area(self): pass

class Square(ShapePoly):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2

# 37. Create two unrelated classes with the same method name and call them in a loop.
class Cat:
    def sound(self): print("Meow")

class DogPoly:
    def sound(self): print("Bark")

for animal in [Cat(), DogPoly()]:
    animal.sound()

# 38. Create a polymorphic function that accepts multiple object types.
def polymorphic_func(obj):
    print(obj.__class__.__name__, "object passed")

# 39. Create a base class with a method, and override it differently in each child class.
class AnimalPoly:
    def speak(self): print("Animal speaks")

class DogPoly2(AnimalPoly):
    def speak(self): print("Dog barks")

class CatPoly(AnimalPoly):
    def speak(self): print("Cat meows")

# 40. Create a method that behaves differently depending on input type.
class Overloaded:
    def process(self, data):
        if isinstance(data, int):
            print("Integer:", data * 2)
        elif isinstance(data, str):
            print("String:", data.upper())

# 41. Write a class that hides a variable using encapsulation (__var).
class Encapsulated:
    def __init__(self):
        self.__secret = "hidden"

    def reveal(self): return self.__secret

# 42. Use getter and setter methods to manage private attributes.
class Account:
    def __init__(self):
        self.__balance = 0

    def set_balance(self, amount):
        if amount >= 0: self.__balance = amount
    def get_balance(self): return self.__balance

# 43. Demonstrate use of @property decorator to control attribute access.
class StudentProp:
    def __init__(self, marks): self._marks = marks

    @property
    def marks(self): return self._marks

    @marks.setter
    def marks(self, val):
        if val >= 0: self._marks = val

# 44. Make a secure login system using encapsulation.
class SecureLogin:
    def __init__(self, password):
        self.__password = password

    def login(self, pwd):
        return self.__password == pwd

# 45. Protect class variables using name mangling and explain it.
class Mangling:
    def __init__(self):
        self.__var = 10

# ====================================================
# E. Advanced OOP (5 Questions)
# ====================================================

# 46. Implement operator overloading for a custom class.
class Vector:
    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, other): return Vector(self.x + other.x, self.y + other.y)
    def __str__(self): return f"({self.x}, {self.y})"

# 47. Create a class that uses a static method and class method.
class Utils:
    @staticmethod
    def add(a, b): return a + b

    count = 0
    @classmethod
    def increment(cls): cls.count += 1

# 48. Demonstrate use of isinstance() and issubclass() in inheritance.
print(isinstance(5, int))         # True
print(issubclass(bool, int))      # True

# 49. Create an abstract base class using abc module and derive it.
from abc import ABC, abstractmethod
class AbstractShape(ABC):
    @abstractmethod
    def area(self): pass

class SquareAbs(AbstractShape):
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2

# 50. Use composition to build a class within another class.
class Engine:
    def start(self): print("Engine starting...")

class CarComp:
    def __init__(self):
        self.engine = Engine()
    def drive(self):
        self.engine.start()
        print("Car driving...")
