# What is encapsulation?
# Encapsulation is the concept of wrapping data (variables) and methods (functions) into a single unit (class).
# It also controls access to the data using access modifiers.

# Access Modifiers:
# Public: No underscore prefix – accessible everywhere.
# Protected: Single underscore prefix (_) – accessible within the class and subclasses.
# Private: Double underscore prefix (__) – accessible only within the class (name mangling is applied).


class Father:

    def __init__(self):
        self.father_name = input("Enter father's name: ")       # Public attribute
        self._balance = int(input("Enter father's bank balance: "))  # Protected attribute
        self.__phone = input("Enter father's phone model: ")    # Private attribute

    def display_father_info(self):
        print(f"Father's Name       : {self.father_name}")
        print(f"Father's Bank Balance: {self._balance}")
        print(f"Father's Phone Model : {self.__phone}")


class Child(Father):
    
    def __init__(self):
        super().__init__()
        self.child_name = input("Enter child's name: ")

    def display_child_info(self):
        print(f"Child's Name        : {self.child_name}")
        print(f"Accessing Father's Bank Balance (Protected): {self._balance}")
        # print(self.__phone)  # This will raise an error (private attribute not accessible)


# Run the program
child = Child()
print("\n--- Child's Info ---")
child.display_child_info()

print("\n--- Father's Info ---")
child.display_father_info()
