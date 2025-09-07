"""
Project: Calendar Event Manager (OOP in Python)

Category: Date, Time & Utility-Based OOP Tasks

Explanation:
------------
This project simulates a simple calendar system where you can manage both 
recurring and one-time events. It demonstrates how OOP principles are applied 
to real-world scenarios like scheduling.

OOP Concepts Used:
------------------
1. Encapsulation → Event details (title, time, frequency) are kept inside classes.  
2. Abstraction   → The Event base class defines the interface (occurs_on) without implementation.  
3. Inheritance   → OneTimeEvent and RecurringEvent extend Event.  
4. Polymorphism  → occurs_on() behaves differently for one-time and recurring events.  

Main Classes:
-------------
1. Event (Abstract Base Class)
   - Defines common attributes and abstract method occurs_on().
   - Provides string representation.

2. OneTimeEvent (Derived Class)
   - Inherits from Event.
   - Represents events that occur only once.

3. RecurringEvent (Derived Class)
   - Inherits from Event.
   - Represents recurring events (daily, weekly, monthly).

4. CalendarEventManager
   - Stores and manages all events.
   - Allows adding events, listing them, and checking what happens on a given date.
"""

from abc import ABC, abstractmethod
from datetime import datetime

# ---------- Abstraction ----------
class Event(ABC):
    def __init__(self, title, start_time):
        self.title = title
        self.start_time = start_time

    @abstractmethod
    def occurs_on(self, date: datetime) -> bool:
        """Check if event occurs on a given date."""
        pass

    def __str__(self):
        return f"{self.title} at {self.start_time.strftime('%Y-%m-%d %H:%M')}"

# ---------- One-Time Event ----------
class OneTimeEvent(Event):
    def occurs_on(self, date: datetime) -> bool:
        return self.start_time.date() == date.date()

# ---------- Recurring Event ----------
class RecurringEvent(Event):
    def __init__(self, title, start_time, frequency: str):
        super().__init__(title, start_time)
        self.frequency = frequency.lower()  # daily, weekly, monthly

    def occurs_on(self, date: datetime) -> bool:
        if self.frequency == "daily":
            return date >= self.start_time
        elif self.frequency == "weekly":
            return (date >= self.start_time) and ((date - self.start_time).days % 7 == 0)
        elif self.frequency == "monthly":
            return (date >= self.start_time) and (self.start_time.day == date.day)
        return False

    def __str__(self):
        return f"{self.title} (Recurring: {self.frequency}) starting {self.start_time.strftime('%Y-%m-%d %H:%M')}"

# ---------- Calendar Event Manager ----------
class CalendarEventManager:
    def __init__(self):
        self.events = []

    def add_event(self, event: Event):
        self.events.append(event)
        print(f" Added: {event}")

    def get_events_on(self, date: datetime):
        """Return all events happening on a specific date."""
        return [event for event in self.events if event.occurs_on(date)]

    def show_all_events(self):
        if not self.events:
            print(" No events scheduled.")
        else:
            print("\n All Events:")
            for event in self.events:
                print(f"- {event}")


# ==============================
# Example Usage
# ==============================
if __name__ == "__main__":
    manager = CalendarEventManager()

    # Add one-time event
    event1 = OneTimeEvent("Doctor Appointment", datetime(2025, 9, 10, 15, 30))
    manager.add_event(event1)

    # Add recurring daily event
    event2 = RecurringEvent("Gym Workout", datetime(2025, 9, 5, 7, 0), "daily")
    manager.add_event(event2)

    # Add recurring weekly event
    event3 = RecurringEvent("Team Meeting", datetime(2025, 9, 3, 10, 0), "weekly")
    manager.add_event(event3)

    # Show all events
    manager.show_all_events()

    # Check events on a specific date
    check_date = datetime(2025, 9, 10)
    print(f"\n Events on {check_date.date()}:")
    for e in manager.get_events_on(check_date):
        print(f"- {e}")
