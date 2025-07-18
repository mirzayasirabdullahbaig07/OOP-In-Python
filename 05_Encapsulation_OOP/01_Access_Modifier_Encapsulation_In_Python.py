# What is Encapsulation in Python?

# Encapsulation is the concept of wrapping data (variables) and code (methods) into a single unit — a class.

# It restricts direct access to some of an object's components, which is a way of preventing accidental modification.

# What are Access Modifiers?
# Access modifiers define how the members (variables/methods) of a class can be accessed.

# Python provides three types:
# - Public: Accessible from anywhere (`self.name`)

# - Protected: Indicated by a single underscore `_var`, meant for internal use, but still accessible

# - Private: Indicated by a double underscore `__var`, name mangled to prevent direct access

from random import randint

class Bank:
    def __init__(self) -> None:
        self.name = input("Enter your name: ")           # Public attribute
        self.__account_no = randint(100000, 999999)      # Private attribute
        self.__balance = 0                               # Private attribute

    def display_balance(self):  # Getter
        print(f"Balance: {self.__balance}")

    def set_balance(self, new_amount):  # Setter
        if new_amount >= 0:
            self.__balance = new_amount
        else:
            print("Invalid balance amount.")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Account No: {self.__account_no}")
        print(f"Balance: {self.__balance}")

# Creating an object of the Bank class
obj = Bank()

# Display account details
obj.display()

# Attempting to modify a private attribute directly (Not recommended)
obj.__account_no = 2   # This creates a new public attribute, doesn't modify the actual __account_no
obj.display()

# Recommended way to update and display balance
# obj.set_balance(1000)
# obj.display_balance()

# Accessing private variable using name mangling (Not recommended)
# print(obj._Bank__balance)  # Technically works, but breaks encapsulation
