"""
Project: NotificationSystem with OOP in Python

Category: Encapsulation, Abstraction, Inheritance, Polymorphism

This project demonstrates how to build a notification system using the four pillars of OOP:
1. Encapsulation   → wrapping notification details inside classes
2. Abstraction     → defining abstract class Notification with abstract send() method
3. Inheritance     → EmailNotification, SMSNotification, PushNotification inherit from Notification
4. Polymorphism    → same method name send() behaves differently for each notification type

We also build a NotificationSystem manager to broadcast messages using all notification types.
"""

from abc import ABC, abstractmethod   # Importing Abstract Base Class tools
import random                         # For simulating random users/messages
import time                           # For adding artificial delay (simulation)


"""
STEP 1: Create an Abstract Base Class for Notification

- This defines the blueprint of any notification type.
- It forces child classes (Email, SMS, Push) to implement the send() method.
- Abstraction ensures that we hide implementation details and only provide the required method.
"""
class Notification(ABC):
    @abstractmethod
    def send(self, message: str, recipient: str):
        """
        Abstract method.
        Every notification type must implement this method.
        Parameters:
        - message (str): The content of the notification
        - recipient (str): The target recipient (email, phone, username, etc.)
        """
        pass


"""
STEP 2: Create EmailNotification class (Inheritance + Polymorphism)

- This class inherits from Notification.
- Implements its own version of send().
- Demonstrates polymorphism because send() is implemented differently than SMS or Push.
"""
class EmailNotification(Notification):
    def send(self, message: str, recipient: str):
        print(f"[EMAIL] Sending email to {recipient}...")
        time.sleep(1)  # Simulate sending delay
        print(f"[EMAIL] Subject: Notification Alert\n[EMAIL] Body: {message}\n")


"""
STEP 3: Create SMSNotification class

- Inherits from Notification.
- Implements send() specifically for SMS.
"""
class SMSNotification(Notification):
    def send(self, message: str, recipient: str):
        print(f"[SMS] Sending SMS to {recipient}...")
        time.sleep(1)  # Simulate delay
        print(f"[SMS] Message: {message}\n")


"""
STEP 4: Create PushNotification class

- Inherits from Notification.
- Implements send() specifically for Push notifications.
"""
class PushNotification(Notification):
    def send(self, message: str, recipient: str):
        print(f"[PUSH] Sending push notification to {recipient}...")
        time.sleep(1)
        print(f"[PUSH] Notification: {message}\n")


"""
STEP 5: Create NotificationSystem Manager Class

- Encapsulation is used here: notifications list is stored inside the class.
- It has methods to:
  1. add_notification() → register a new notification method (Email, SMS, Push, etc.)
  2. broadcast() → send a single message to a recipient through ALL registered notification types.
"""
class NotificationSystem:
    def __init__(self):
        # List to store different notification objects (Email, SMS, Push)
        self.notifications = []

    def add_notification(self, notification: Notification):
        """
        Adds a notification type (object of EmailNotification, SMSNotification, etc.)
        """
        self.notifications.append(notification)

    def broadcast(self, message: str, recipient: str):
        """
        Sends the same message to a recipient using all registered notifications.
        Demonstrates polymorphism: the same send() method is called,
        but actual behavior depends on the notification object.
        """
        print(f"\n--- Broadcasting message to {recipient} ---")
        for notifier in self.notifications:
            notifier.send(message, recipient)


"""
STEP 6: Main Program Simulation

- Create an instance of NotificationSystem.
- Add Email, SMS, and Push notifications to it.
- Define a list of users (recipients).
- Define a list of messages to be sent.
- Randomly pick users and messages to simulate real-world broadcasting.
"""
if __name__ == "__main__":
    # Create notification system
    system = NotificationSystem()

    # Add notification methods
    system.add_notification(EmailNotification())
    system.add_notification(SMSNotification())
    system.add_notification(PushNotification())

    # Example recipients
    users = ["alice@example.com", "bob@example.com", "charlie@example.com"]

    # Example messages
    messages = [
        "Your order has been shipped!",
        "Your OTP code is 123456",
        "New login from unknown device",
        "Flash Sale: 50% off today only!"
    ]

    # Randomly send messages to users
    for i in range(3):  # send 3 broadcasts
        user = random.choice(users)
        message = random.choice(messages)
        system.broadcast(message, user)
        print("-" * 50)
