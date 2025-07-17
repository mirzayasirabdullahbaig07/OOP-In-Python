# ------------------------------
# What is a module in Python?
# ------------------------------
# A module in Python is a file containing Python definitions and functions.
# You can reuse the functions in another Python file by importing the module.

# ------------------------------
# Example Module: area_shapes.py
# ------------------------------

# Function to calculate the area of a circle
def circle(radius: float) -> None:
    area = 3.14 * radius * radius
    print(f"Area of circle with radius {radius} = {area}")


# Function to calculate the area of a rectangle
def rectangle(length: float, breadth: float) -> None:
    area = length * breadth
    print(f"Area of rectangle = {area}")


# Function to calculate the area of a triangle
def triangle(base: float, height: float) -> None:
    area = 0.5 * base * height
    print(f"Area of triangle = {area}")


# ------------------------------
# Concept: if __name__ == "__main__"
# ------------------------------
# This block runs only when the file is executed directly.
# It does NOT run when the file is imported as a module into another script.
# This is useful for testing or demo purposes.

if __name__ == "__main__":
    circle(56.474)
    rectangle(23, 42)
    triangle(10, 5)
