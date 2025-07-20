# What are Generators in Python?

# Generators are functions that return an iterator and allow us to iterate through a sequence of values,
# one at a time, using the 'yield' keyword instead of 'return'.
# Unlike lists, generators don’t store the entire sequence in memory — they generate values on the fly.

# Why/Where do we use Generators?
# - To save memory when dealing with large data streams
# - To improve performance with lazy evaluation
# - To create custom iterators easily

# Generator vs Normal Function:
# - Normal function → returns result using `return` (all at once)
# - Generator function → uses `yield` to return values one by one on demand


# Example 1: A simple generator that yields numbers from 1 to 5

def number_generator():
    for i in range(1, 6):
        yield i

gen = number_generator()

for num in gen:
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5


# Example 2: Generator to generate even numbers up to a given limit

def even_numbers(limit):
    for i in range(2, limit + 1, 2):
        yield i

gen = even_numbers(10)

for even in gen:
    print(even)

# Output:
# 2
# 4
# 6
# 8
# 10
