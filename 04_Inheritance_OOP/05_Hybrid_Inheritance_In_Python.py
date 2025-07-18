# What is Hybrid Inheritance in Python?

# Hybrid Inheritance is a combination of two or more types of inheritance (like single, multiple, multilevel, or hierarchical) in a single program.

# It’s called "hybrid" because it mixes different inheritance structures.

# example

class A:
    def show_A(self):
        print("Class A")

class B(A):
    def show_B(self):
        print("Class B")

class C(A):
    def show_C(self):
        print("Class C")

class D(B, C):  # Hybrid: multilevel + multiple + hierarchical
    def show_D(self):
        print("Class D")


# Create object of D
obj = D()

# Access all inherited methods
obj.show_A()  # From A
obj.show_B()  # From B
obj.show_C()  # From C
obj.show_D()  # From D
