"""
Project: E-Commerce Backend with OOP in Python

Category: Encapsulation, Abstraction, Inheritance, Polymorphism

We will build an E-Commerce backend system with:
1. Product class → represents items sold
2. Customer class → represents customers
3. Order class → manages customer orders with products

We will simulate:
- Adding products to catalog
- Registering customers
- Creating orders
- Displaying order details
"""


import datetime   # to track order date/time
import random     # to generate unique IDs


"""
STEP 1: Define the Product Class
- Represents an item that can be sold.
- Each product has an id, name, price, and stock quantity.
- Methods:
    1. update_stock(): reduces stock after purchase.
    2. __str__(): displays product details.
"""
class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.product_id = random.randint(1000, 9999)  # Unique ID
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity: int):
        """Reduce stock when purchased"""
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        else:
            return False

    def __str__(self):
        return f"Product[{self.product_id}] {self.name} - ${self.price} (Stock: {self.stock})"


"""
STEP 2: Define the Customer Class
- Represents a registered customer.
- Each customer has an id, name, email, and a purchase history.
"""
class Customer:
    def __init__(self, name: str, email: str):
        self.customer_id = random.randint(10000, 99999)
        self.name = name
        self.email = email
        self.orders = []   # list of Order objects

    def add_order(self, order):
        """Adds an order to customer history"""
        self.orders.append(order)

    def __str__(self):
        return f"Customer[{self.customer_id}] {self.name} ({self.email})"


"""
STEP 3: Define the Order Class
- Represents an order placed by a customer.
- Each order has an order_id, customer, list of items, total amount, and date.
- Methods:
    1. add_item() → add product & quantity
    2. calculate_total() → compute total price
    3. display_order() → show order details
"""
class Order:
    def __init__(self, customer: Customer):
        self.order_id = random.randint(100000, 999999)
        self.customer = customer
        self.items = []     # list of tuples (Product, quantity)
        self.total = 0.0
        self.date = datetime.datetime.now()

    def add_item(self, product: Product, quantity: int):
        """Add a product to the order"""
        if product.update_stock(quantity):
            self.items.append((product, quantity))
            self.calculate_total()
            print(f"[ORDER] Added {quantity} x {product.name} to order {self.order_id}")
        else:
            print(f"[ERROR] Not enough stock for {product.name}")

    def calculate_total(self):
        """Calculate total cost"""
        self.total = sum(p.price * q for p, q in self.items)

    def display_order(self):
        """Print order summary"""
        print("\n===== ORDER SUMMARY =====")
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer.name}")
        print(f"Date: {self.date.strftime('%Y-%m-%d %H:%M:%S')}")
        print("\nItems:")
        for product, qty in self.items:
            print(f"- {product.name} (x{qty}) = ${product.price * qty}")
        print(f"\nTOTAL: ${self.total}")
        print("=========================\n")


"""
STEP 4: Simulate the E-Commerce System
- Create products
- Create customers
- Place orders
- Display results
"""
if __name__ == "__main__":
    # Create sample products
    laptop = Product("Laptop", 1200.0, 5)
    phone = Product("Smartphone", 800.0, 10)
    headphones = Product("Headphones", 150.0, 20)

    # Display products
    print(laptop)
    print(phone)
    print(headphones)

    # Create a customer
    customer1 = Customer("Alice Johnson", "alice@example.com")
    print(customer1)

    # Create an order for customer1
    order1 = Order(customer1)

    # Add items to order
    order1.add_item(laptop, 1)
    order1.add_item(phone, 2)
    order1.add_item(headphones, 3)

    # Attach order to customer history
    customer1.add_order(order1)

    # Display final order summary
    order1.display_order()
