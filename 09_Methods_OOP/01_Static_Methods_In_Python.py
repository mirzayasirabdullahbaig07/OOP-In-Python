# What are Static Methods?

# Static methods in Python are methods that do not require access to the instance (self)
# or class (cls). These methods are bound to a class, not to its object.
# They are defined using the @staticmethod decorator.
# 
# Why do we use static methods?
# - When the method does not need to access or modify instance/class attributes.
# - To perform utility operations related to the class.
# - Helps in keeping related logic within the class without using its state.

from datetime import datetime

class calender():
    def __init__(self) -> None:
        self.events = []

    def add_event(self, event_name):
        self.events.append(event_name)

    def display_events(self):
        print(f"events = {self.events}")

    @staticmethod
    def is_weekened(date: datetime):
        # This method does not use self or cls
        # It checks whether the given date is a weekend or not
        if date.weekday() > 4:
            print("it is a weekend")
        else:
            print("it is a day")

# Creating object of class
ob1 = calender()
ob1.add_event("party")
ob1.add_event("dsa")
ob1.add_event("coding")
ob1.display_events()

# Calling static method directly using class name (no need to create object)
current_date = datetime.now()
calender.is_weekened(current_date)

# This is all about the Static Methods
