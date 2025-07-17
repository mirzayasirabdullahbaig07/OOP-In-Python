# ------------------------------
# 1. Positional vs Named Arguments
# ------------------------------

def total_marks(maths, science, english, urdu, history):
    total = maths + science + english + urdu + history
    print(total)

# Positional Arguments (order matters)
total_marks(84, 65, 67, 54, 75)

# Named Arguments (order doesn't matter)
total_marks(maths=100, urdu=14, english=13, science=29, history=32)

# ❌ Mixing positional after named is not allowed
# total_marks(maths=100, 54, 483)  # Error


# ------------------------------
# 2. Default Arguments
# ------------------------------

def add_default(n1, n2):
    print(n1 + n2)

add_default(11, 32)

# def add_default(n1, n2=3):
#     print(n1 + n2)

# add_default()  # Error: missing required positional argument n1


# ------------------------------
# 3. *args (Variable-Length Positional Arguments)
# ------------------------------

def add_fixed(n1, n2, n3):
    total = n1 + n2 + n3
    print(total)

add_fixed(23, 243, 2)
# add_fixed(1, 3, 5, 3, 6, 3, 3, 5)  # Error: too many arguments
# add_fixed(2, 4)  # Error: missing one argument

# Using *args to accept variable number of arguments
def add_varargs(*args):
    print(sum(args))

add_varargs(23, 243, 2)
add_varargs(1, 3, 5, 3, 6, 3, 3, 5)
add_varargs(2, 4)


# ------------------------------
# 4. **kwargs (Variable-Length Keyword Arguments)
# ------------------------------

def add_kwargs(**kwargs):
    print(kwargs)

add_kwargs(name="yasir", age="24", gender="male")

# Iterating through kwargs

def display_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

display_kwargs(name="yasir", age="24", gender="male")


# ------------------------------
# 5. Mixed Parameters Example
# ------------------------------

def add_mixed(n1, n2, n3, *args, **kwargs):
    print(f"n1 = {n1}")
    print(f"n2 = {n2}")
    print(f"n3 = {n3}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")
    if 'name' in kwargs:
        print(f"name = {kwargs['name']}")

add_mixed(2, 4, 5, 199, 4003)
# add_mixed(2,4,5,199,4003, n=22)  # Error: positional argument follows keyword
add_mixed(2, 4, 5, 199, 4003, 2434, 22, name="yasir", education="software high class")


# ------------------------------
# 6. Lambda Functions (Anonymous Functions)
# ------------------------------

def add_normal(n1, n2, n3):
    return n1 + n2 + n3

x = add_normal(2, 3, 5)
print(x)

# Lambda function
abc = lambda n1, n2, n3: n1 + n2 + n3
print(abc(2, 3, 5))

# Lambda: Generate list from 0 to n
sum_list = lambda n: [i for i in range(0, n + 1)]
list1 = sum_list(67)
list2 = sum_list(23)
print(f"list1 = {list1}")
print(f"list2 = {list2}")

# Lambda: Generate list from 0 to user input
sum_list = lambda n: [i for i in range(0, n + 1)]
number = int(input("Enter the value: "))
list1 = sum_list(number)
list2 = sum_list(number)
print(f"list1 = {list1}")
print(f"list2 = {list2}")

# Lambda: Check even or odd
check_even = lambda num: num % 2 == 0
enter_num = int(input("Enter the number: "))
if check_even(enter_num):
    print("even")
else:
    print("odd")

# Lambda with ternary operator
check_num = lambda num: print("even") if num % 2 == 0 else print("odd")
number = int(input("Enter the number: "))
check_num(number)


# ------------------------------
# 7. Function Annotations
# ------------------------------

def add_simple(x, y):
    total = x + y
    print(total)

add_simple(3, 4)

# With annotation
def add_annotated(x: int, y: int):
    total = x + y
    print(total)

add_annotated(3, 4)

# With annotation and return
def add_return(x: int, y: int) -> int:
    total = x + y
    return total

q = add_return(3, 4)
print(q)


# ------------------------------
# 8. Sorting and Counting in List
# ------------------------------

list2 = [14, 9838, 3632, 28, 373, 1999]
list2.sort()
print(list2)

c = list2.count(14)
print(c)


# ------------------------------
# 9. Complete Example with Annotations
# ------------------------------

def add_final(x: int, y: int) -> int:
    total = x + y
    return total

def greet(name: str, age: int, percentage: float) -> None:
    print(age)
    print(name)
    print(percentage)

b = add_final(2, 4)
print(b)
greet("Ali", 24, 95.4)


# ------------------------------
# 10. Type Hinting with List from typing
# ------------------------------

from typing import List

def sum_of_list(x: List[int]):
    print(sum(x))

sum_of_list([1, 2, 3, 4, 5])
sum_of_list([43, 54])