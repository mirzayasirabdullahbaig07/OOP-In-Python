"""
Project: File Handling System with OOP in Python

Category: Encapsulation, Abstraction, Inheritance, Polymorphism

Explanation:
------------
This project demonstrates file reading and writing operations using Object-Oriented Programming.  
It applies all four pillars of OOP:
    - Encapsulation
    - Abstraction
    - Inheritance
    - Polymorphism

Main Classes:
1. FileHandler (Abstract Base Class)
   - Methods: read(), write()
   - Defines the interface for file operations (Abstraction)

2. TextFileHandler (Derived Class)
   - Inherits FileHandler
   - Implements read() and write() for `.txt` files

3. JSONFileHandler (Derived Class)
   - Inherits FileHandler
   - Implements read() and write() for `.json` files

OOP Concepts Used:
------------------
1. Encapsulation → File details hidden inside handler classes.  
2. Abstraction   → FileHandler defines interface but not implementation.  
3. Inheritance   → Subclasses extend FileHandler.  
4. Polymorphism  → read() and write() behave differently for text vs JSON files.

Note:
-----
This is a simplified simulation for learning OOP, not a complete file management system.
"""

import json
from abc import ABC, abstractmethod

# ---------- Abstraction ----------
class FileHandler(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


# ---------- Text File Handler ----------
class TextFileHandler(FileHandler):
    def read(self):
        with open(self.filename, "r") as file:
            return file.read()

    def write(self, data):
        with open(self.filename, "w") as file:
            file.write(data)
        print(f"Written text data to {self.filename}")


# ---------- JSON File Handler ----------
class JSONFileHandler(FileHandler):
    def read(self):
        with open(self.filename, "r") as file:
            return json.load(file)

    def write(self, data):
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Written JSON data to {self.filename}")


# ---------- Example Usage ----------
if __name__ == "__main__":
    # Text file example
    text_handler = TextFileHandler("example.txt")
    text_handler.write("Hello, this is a text file!")
    print("Text File Content:", text_handler.read())

    # JSON file example
    json_handler = JSONFileHandler("example.json")
    json_handler.write({"name": "Yasir", "role": "Developer"})
    print("JSON File Content:", json_handler.read())
