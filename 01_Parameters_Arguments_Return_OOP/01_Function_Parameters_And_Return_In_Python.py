# Lecture 1: Functions in Python

# -------------------------------
# What are functions?
# -------------------------------
# A function is a reusable block of code that performs a specific task when called.
# There are two types of functions:
# 1. Built-in functions (e.g., print(), len(), input(), etc.)
# 2. User-defined functions (functions you define yourself)

# -------------------------------
# Functions vs Methods
# -------------------------------
# Functions: Pre-defined or user-defined blocks of code that can be called independently.

print("Yasir")  # 'print' is a built-in function.

# Methods: Functions associated with objects/data types.
# Example: list.append(), str.upper(), dict.get(), etc.

# -------------------------------
# User-defined Function Example
# -------------------------------

def greet():
    print("My name is Yasir Abdullah")
    print("I am a Software Engineer")
    print("I am learning Machine Learning and Deep Learning")

# Calling the function
greet()

# -------------------------------
# Variable Scope in Functions
# -------------------------------

def addition():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"The sum is: {num1 + num2}")

addition()

# Uncommenting the next line will cause an error because 'num1' is not accessible outside the function.
# print(num1)

# -------------------------------
# Using Multiple Functions
# -------------------------------

def addition():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"The sum is: {num1 + num2}")

def subtraction():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"The difference is: {num1 - num2}")

# Call the functions
addition()
subtraction()

# -------------------------------
# Scope Example with Same Variable Name
# -------------------------------

def greet():
    name = input("Enter your name: ")
    print("Inside function, name is:", name)

name = "Abdullah"
greet()
print("Outside function, name is:", name)

# -------------------------------
# Types of Functions
# -------------------------------
# Based on Parameters and Return Values:
# 1. No parameters, no return
# 2. With parameters, no return
# 3. No parameters, with return
# 4. With parameters, with return

# -------------------------------
# Function with Parameters (No Return)
# -------------------------------

def addition(n1, n2):
    total = n1 + n2
    print(f"Sum is: {total}")

addition(2, 4)

# -------------------------------
# Mismatch in Parameters vs Arguments
# -------------------------------
# The number of arguments must match the number of parameters.

# def addition(n1, n2):
#     total = n1 + n2
#     print(total)
# addition(2, 4, 3)  # This will throw an error (too many arguments)

# -------------------------------
# List Sum Example with Logic
# -------------------------------

def addition_list(numbers):
    total = 0
    for num in numbers:
        total += num
    print(f"Sum of list: {total}")

my_list = [1, 2, 3, 5, 6]
addition_list(my_list)

# -------------------------------
# Function with Return Value
# -------------------------------

def addition(n1, n2):
    total = n1 + n2
    return total

# Store return in a variable
result = addition(2, 4)
print(f"Returned result: {result}")

# Or directly print the returned value
print(f"Direct return: {addition(2, 4)}")

# -------------------------------
# Function Without Return
# -------------------------------

def addition(n1, n2):
    total = n1 + n2
    print(f"Printed result: {total}")

x = addition(2, 4)
print(f"Returned value: {x}")  # Will print 'None'

# -------------------------------
# When to Use Return vs Print
# -------------------------------
# Use 'return' when you need to use the result later.
# Use 'print' when you just want to display something immediately.

# -------------------------------
# Realistic Use Case
# -------------------------------
# 1. Ask for two numbers from the user
# 2. Calculate their sum
# 3. Check if the result is even or odd

def addition(n1, n2):
    return n1 + n2

def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Processing
result = addition(num1, num2)
check_even_odd(result)
