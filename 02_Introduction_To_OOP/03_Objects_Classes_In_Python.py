# what is classes and object?
class Student:
    def __init__(self) -> None:
        self.name = input("Enter Name = ")
        self.age = int(input("Enter age = "))

    def display_info(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
    
    def change_name(self, change_name):
        self.name = change_name
    

s1 = Student()
s1.display_info()
s1.change_name("xyz")
s1.display_info()