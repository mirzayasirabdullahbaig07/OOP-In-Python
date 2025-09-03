"""
Project: Zoo Simulation with OOP in Python

Category: Encapsulation, Abstraction, Inheritance, Polymorphism

Explanation:
------------
This project simulates a Zoo environment with different animals using Object-Oriented Programming concepts.  
We focus especially on **Inheritance** to model common and specific animal behaviors.

Main Classes:
1. Animal (Base Class)
   - Attributes: name, species
   - Methods: make_sound(), eat()
   - Provides common structure for all animals

2. Derived Classes: Lion, Elephant, Monkey, Bird
   - Each inherits from Animal
   - Each overrides make_sound() method
   - Demonstrates Polymorphism

3. Zoo
   - Maintains a collection of animals
   - Provides methods: add_animal(), show_all_animals()

OOP Concepts Used:
------------------
1. Encapsulation → Each class manages its own data (animal name, sound, etc.).  
2. Abstraction   → The base class defines general methods for all animals.  
3. Inheritance   → All animals inherit from the Animal base class.  
4. Polymorphism  → Each animal makes a different sound, overriding the same method.  

Note:
-----
This is a simplified Zoo simulation to demonstrate OOP principles, not a full simulation game.
"""

# ---------- Animal Base Class ----------
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic animal sound"

    def eat(self):
        return f"{self.name} the {self.species} is eating."


# ---------- Derived Animal Classes ----------
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion")

    def make_sound(self):
        return "Roar!"


class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, "Elephant")

    def make_sound(self):
        return "Trumpet!"


class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name, "Monkey")

    def make_sound(self):
        return "Ooh ooh aah aah!"


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, "Bird")

    def make_sound(self):
        return "Chirp chirp!"


# ---------- Zoo Class ----------
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)
        print(f"{animal.name} the {animal.species} has been added to the zoo.")

    def show_all_animals(self):
        print("\n--- Zoo Animals ---")
        for animal in self.animals:
            print(f"{animal.name} the {animal.species} says {animal.make_sound()} and {animal.eat()}")


# ---------- Example Usage ----------
if __name__ == "__main__":
    zoo = Zoo()

    # Add animals
    zoo.add_animal(Lion("Simba"))
    zoo.add_animal(Elephant("Dumbo"))
    zoo.add_animal(Monkey("George"))
    zoo.add_animal(Bird("Tweety"))

    # Show animals in zoo
    zoo.show_all_animals()
