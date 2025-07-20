# What are Decorators in Python?

# Decorators in Python are functions that modify the behavior of another function 
# without changing its structure. 
# They allow us to "wrap" another function to add extra functionality before or after the original function runs.

#   Where can we use decorators?
# - Logging function execution
# - Measuring execution time
# - Access control/authentication
# - Caching or memoization
# - Pre/post-processing around functions

# Syntax:
# A decorator is usually applied using the '@decorator_name' above the function definition.


# Example 1: Basic decorator to log function call

def log_decorator(func):
    def wrapper():
        print("Function is being called...")
        func()
        print("Function execution finished.")
    return wrapper

@log_decorator
def say_hello():
    print("Hello, World!")

say_hello()


# Output:
# Function is being called...
# Hello, World!
# Function execution finished.


# Example 2: Decorator to check access based on a user role

def check_admin(func):
    def wrapper(role):
        if role == "admin":
            func(role)
        else:
            print("Access denied. Admins only.")
    return wrapper

@check_admin
def delete_data(role):
    print("Data deleted successfully.")

delete_data("admin")   # Allowed
delete_data("guest")   # Denied


# Output:
# Data deleted successfully.
# Access denied. Admins only.
