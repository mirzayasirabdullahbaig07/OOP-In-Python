# What are Dunder Methods in Python?

# Dunder (Double Underscore) methods are special methods in Python that start and end with double underscores (__).
# Example: __init__, __str__, __len__, __add__, etc.

# These methods allow us to define custom behavior for built-in operations like object creation, printing, addition, etc.

class Father:

    def __init__(self):
        """This is a dunder method called automatically when an object is created."""
        self.father_name = input("Enter father's name: ")
        self._balance = int(input("Enter father's bank balance: "))  # Protected attribute
        self.__phone = input("Enter father's phone model: ")         # Private attribute

    def __str__(self):
        """Overrides the default print behavior to show meaningful output."""
        return (
            f"Father's Name: {self.father_name}\n"
            f"Father's Bank Balance: {self._balance}\n"
            f"Father's Phone Model: {self.__phone}"
        )

    # def display_father_info(self):
    #     print(f"Father's Name: {self.father_name}")
    #     print(f"Father's Bank Balance: {self._balance}")
    #     print(f"Father's Phone Model : {self.__phone}")

# Creating object

obj = Father()
# obj.display_father_info()
# This will print formatted details because __str__ is overridden
print(obj)  # it will show id of that obj so we use dender methods






