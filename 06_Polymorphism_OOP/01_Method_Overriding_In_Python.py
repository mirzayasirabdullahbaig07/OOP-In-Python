# What is Method Overriding in Python?
# Method Overriding means providing a new definition for a method in a subclass
# that is already defined in the parent class. It allows different behaviors for the same method name.

# This is a part of Polymorphism (many forms of behavior).

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    # Overriding the 'sound' method of Animal class
    def sound(self):
        print("Dog says: Bhaw Bhaw")

class Cat(Animal):
    # Overriding the 'sound' method of Animal class
    def sound(self):
        print("Cat says: Meow Meow")

# Creating objects of Dog and Cat
dog = Dog()
cat = Cat()

# Method overriding in action
dog.sound()  # Output: Dog says: Bhaw Bhaw
cat.sound()  # Output: Cat says: Meow Meow
