# What is Multilevel Inheritance in Python?
# Multilevel Inheritance means a class is derived from a class which is already derived from another class. It forms a "chain of inheritance" like Grandparent → Parent → Child.

# syntax

class A:
    # Base class
    pass

class B(A):
    # Derived from A
    pass

class C(B):
    # Derived from B (A → B → C)
    pass




class Grandfather:
    def show_grandfather(self):
        print("I am Grandfather")


class Father(Grandfather):
    def show_father(self):
        print("I am Father")


class Son(Father):
    def show_son(self):
        print("I am Son")


# Create object of the lowest child class
s1 = Son()

# Access methods from all levels of inheritance
s1.show_grandfather()  # Inherited from Grandfather
s1.show_father()       # Inherited from Father
s1.show_son()          # Own method
