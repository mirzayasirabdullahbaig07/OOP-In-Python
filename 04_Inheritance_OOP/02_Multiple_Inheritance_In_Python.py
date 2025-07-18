# What is Multiple Inheritance?
# Multiple inheritance means a class can inherit from more than one parent class.
# This allows the child class to access attributes and methods from all parent classes.

class Father():
    father_name = ""  # class attribute

    def FatherNameDisplay(self):  # method to print father's name
        print(self.father_name)

# Parent class 2
class Mother():
    mother_name = ""  # class attribute

    def MotherNameDisplay(self):  # method to print mother's name
        print(self.mother_name)

# Child class inheriting from both Father and Mother
class Child(Father, Mother):
    child_name = ""  # class attribute

    def ChildNameDisplay(self):  # method to print child's name
        print(self.child_name)

# Object of Child class
c1 = Child()
c1.father_name = "Imran"      # inherited from Father
c1.mother_name = "Shazia"     # inherited from Mother
c1.child_name = "Yasir"       # own property

# Calling methods
c1.FatherNameDisplay()        # prints: Imran
c1.MotherNameDisplay()        # prints: Shazia
c1.ChildNameDisplay()         # prints: Yasir
