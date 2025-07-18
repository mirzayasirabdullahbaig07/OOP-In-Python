# # what is inheritance in python oop?
# # it means u can inherit the properity of class a in class b

# # class 1
# # var
# # methods

# # class 2
# # var
# # methods

# # now u can access the obj.var of class 1

# # example of car
# # class car
# # properties of car
# # color
# # type
# # milage
# # seat capacity

# # let suppose

# # class audi
# # we have to use the class properties in the audi class and some other specific information related to the class audi
# # branding
# # model
# # self drive

# # now class maruti
# # we use the same properites of class which is general and we have to add some specific data related to this car
# # it show this is the repeation in the code
# # we have to avoid this and here inheritiance play its role

# # now we inherit the properites of car for any other car like audi or maruti

class Car():
    # method to initialize common car properties
    def __init__(self, color:str, type:str, milage:float, seat_capacity:int) -> None:
        self.color = color
        self.type = type
        self.milage = milage
        self.seat_capacity = seat_capacity # these are class variables

    # method to display common car details
    def base_info(self):
        print(f"color = {self.color}")
        print(f"type = {self.type}")
        print(f"milage = {self.milage}")
        print(f"seat_capacity = {self.seat_capacity}")

class Audi(Car):
    # constructor for Audi class
    def __init__(self):
        print("hello audi")

# # c1 = Car("red", "petrol", "22.5", 4)
# # c1.base_info()

# # c1 = Audi()
# # c1.base_info() # if we do this it will throw an error

# # so we have to add the attributes

c1 = Audi()
c1.color = "Red"
c1.milage = 23.4
c1.type = "petrol"
c1.seat_capacity = 4
c1.base_info()

# now do another example

class Car():
    # method to manually set attributes
    def set_info(self, color:str, milage:float, seats:int, type:str):
        self.color = color
        self.milage = milage
        self.seats = seats
        self.type =  type

    # method to print base car info
    def base_info(self):
        print(f"color = {self.color}")
        print(f"milage = {self.milage}")
        print(f"seats = {self.seats}")
        print(f"type = {self.type}")

class Audi(Car):
    # method to set Audi-specific info along with base info
    def set_audi_info(self, color:str, milage:float, seats:int, type:str, electric:bool, city:str):
        self.set_info(color, milage, seats, type)
        self.electric = electric
        self.city = city

    # method to print Audi-specific info
    def audi_info(self):
        print(f"electric = {self.electric}")
        print(f"city = {self.city}")

class Toyota(Car):
    # method to set Toyota-specific info along with base info
    def toyota_info_set(self, color:str, milage:float, seats:int, type:str, electric:bool, city:str):
        self.set_info(color, milage, seats, type)
        self.electric = electric
        self.city = city

    # method to print Toyota-specific info
    def toyota_info(self):
        print(f"electric = {self.electric}")
        print(f"city = {self.city}")

c1 = Audi()
c1.set_audi_info("black", 23.4, 4, "petrol", True, "Karachi")
c1.base_info()

print("-----------------------------")

c2 = Toyota()
c2.toyota_info_set("blue", 24.1, 5, "desil", False, "Lahore")
c2.base_info()

# another method

class Car():
    # method to take input for base car attributes
    def set_info(self):
        self.color = input("Enter car color = ")
        self.type = input("Enter type = ")
        self.mileage = float(input("Enter mileage = "))
        self.seat_capacity = int(input("Enter seat capacity = "))

    # method to print base car info
    def base_info(self):
        print(f"color = {self.color}")
        print(f"type = {self.type}")
        print(f"mileage = {self.mileage}")
        print(f"seat_capacity = {self.seat_capacity}")

class Audi(Car):
    # method to take input for audi-specific and base attributes
    def set_audi_info(self):
        self.set_info()
        self.electric = input("Enter electric = ")
        self.city = input("Enter city = ")

    # method to print audi-specific info
    def audi_info(self):
        print(f"Electric = {self.electric}")
        print(f"City = {self.city}")

    # method to show full info
    def show_full_info(self):
        self.base_info()
        self.audi_info()

# Main execution
c1 = Audi()
c1.set_audi_info()
# c1.base_info()
c1.show_full_info()

# using init
class Car:
    # constructor for base car info with input
    def __init__(self) -> None:
        self.color = input("Enter car color = ")
        self.type = input("Enter type = ")
        self.mileage = float(input("Enter mileage = "))
        self.seat_capacity = int(input("Enter seat capacity = "))

    # method to print base car info
    def base_info(self):
        print(f"Color = {self.color}")
        print(f"Type = {self.type}")
        print(f"Mileage = {self.mileage}")
        print(f"Seat capacity = {self.seat_capacity}")

class Audi(Car):
    # constructor for Audi with super() to initialize base + specific
    def __init__(self) -> None:
        super().__init__()
        self.electric = input("Enter electric = ")
        self.city = input("Enter city = ")

    # method to print audi-specific info
    def audi_info(self):
        print(f"Electric = {self.electric}")
        print(f"City = {self.city}")

    # method to print full car info
    def show_full_info(self):
        self.base_info()
        self.audi_info()

# Example usage
c1 = Audi()
c1.base_info()
c1.audi_info()
