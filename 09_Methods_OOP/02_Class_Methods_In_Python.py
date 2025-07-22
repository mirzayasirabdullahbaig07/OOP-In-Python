# What is a Class Method in Python?

# A class method is a method that is bound to the class and not the instance of the class.
# It takes `cls` (the class itself) as its first parameter instead of `self`.
# It is defined using the @classmethod decorator.

# Why do we use Class Methods / Factory Methods?

# - To create multiple ways of initializing objects (known as Factory Methods).
# - When you want to perform some operations that relate to the class as a whole.
# - Useful for alternative constructors like creating objects from files, strings, etc.

class Student:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My gender is {self.gender}")

    @classmethod
    def create_student_using_params(cls, name, age, gender):
        # Factory method to create Student object using given parameters
        obj = cls(name, age, gender)
        return obj
    
    @classmethod
    def create_student_using_file(cls, filename):
        # Factory method to create Student object by reading data from a file
        f = open(filename, 'r')
        student_data = f.read()
        name, age, gender = student_data.split()
        f.close()
        obj = cls(name, age, gender)
        return obj

# Creating student object using factory method with direct parameters
obj1 = Student.create_student_using_params('Yasir', 24, 'Male')
obj1.display()

# Creating student object using factory method with data from a file
# Make sure 'student.txt' contains: Yasir 24 Male
obj2 = Student.create_student_using_file("student.txt")
obj2.display()


# You could also create the object like this (normal way):
# obj1 = Student("Yasir", 24, "Male")
# obj1.display()

# This is all about the Class Methods
