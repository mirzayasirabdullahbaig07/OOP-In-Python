"""
Project: ShoppingCart  with OOP in Python

Category: Encapsulation, Abstraction, Inheritance, Polymorphism

Problem Statement:

Create a ShoppingCart system using Object-Oriented Programming (OOP)
principles in Python. The system should allow:

1. Products (with name and price).
2. Support for both:
   - Regular Products (no discount).
   - Discounted Products (percentage discount).
3. A ShoppingCart where:
   - Items can be added.
   - The total bill can be calculated.

We must demonstrate the OOP concepts:
- Encapsulation (hiding internal details using protected/private variables).
- Abstraction (abstract base class for Product).
- Inheritance (RegularProduct and DiscountedProduct inherit Product).
- Polymorphism (different `get_price()` implementations for each product).


------------------------------------------------------------
Approach:
------------------------------------------------------------
1. Create an abstract base class `Product`:
   - Encapsulate name and price as protected attributes (`_name`, `_price`).
   - Define an abstract method `get_price()` for subclasses to implement.

2. Create `RegularProduct` subclass:
   - Inherits Product.
   - Returns price directly in `get_price()`.

3. Create `DiscountedProduct` subclass:
   - Inherits Product.
   - Adds discount attribute.
   - Overrides `get_price()` to calculate discounted price.

4. Create `ShoppingCart` class:
   - Encapsulates items in a private list.
   - Method `add_item()` to add products.
   - Method `total()` to calculate bill using polymorphism.


------------------------------------------------------------
Dry Run Example:
------------------------------------------------------------
cart = ShoppingCart()
cart.add_item(RegularProduct("Laptop", 1200))
cart.add_item(DiscountedProduct("Headphones", 200, 20))  # 20% off

Step 1: Laptop (RegularProduct) -> get_price() = 1200
Step 2: Headphones (DiscountedProduct) -> get_price() = 200 - (20% of 200) = 160
Step 3: Total = 1200 + 160 = 1360

Final Answer: 1360


------------------------------------------------------------
Complexity Analysis:
------------------------------------------------------------
Time Complexity:
- Adding item: O(1)
- Calculating total: O(n) (iterate through items list)

Space Complexity:
- O(n) for storing products in cart

This is efficient and scalable.
======================================================================
"""

# ---------- Import ABC for Abstraction ----------
from abc import ABC, abstractmethod


# ---------- Abstract Class (Abstraction) ----------
class Product(ABC):
    def __init__(self, name, price):
        # Encapsulation -> Keeping variables protected
        self._name = name
        self._price = price

    # Abstract Method -> Forces subclasses to implement
    @abstractmethod
    def get_price(self):
        pass


# ---------- Regular Product (Inheritance) ----------
class RegularProduct(Product):
    def get_price(self):
        return self._price  # No discount applied


# ---------- Discounted Product (Inheritance + Polymorphism) ----------
class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self._discount = discount

    def get_price(self):
        return self._price - (self._price * self._discount / 100)


# ---------- Shopping Cart (Encapsulation + Polymorphism) ----------
class ShoppingCart:
    def __init__(self):
        self._items = []  # private list of items

    def add_item(self, product: Product):
        self._items.append(product)

    def total(self):
        return sum(item.get_price() for item in self._items)


# ---------- Example Usage ----------
if __name__ == "__main__":
    cart = ShoppingCart()

    # Add products
    cart.add_item(RegularProduct("Laptop", 1200))
    cart.add_item(DiscountedProduct("Headphones", 200, 20))  # 20% off
    cart.add_item(DiscountedProduct("Mouse", 50, 10))        # 10% off

    # Print total
    print("Total Bill:", cart.total())  # Expected: 1200 + 160 + 45 = 1405



# -------------------- Time & Space Complexity --------------------
"""
Time Complexity:
- Adding item to cart -> O(1)
- Calculating total:
    For N items, we call get_price() on each -> O(N)
Overall: O(N)

Space Complexity:
- Cart stores N items -> O(N)
- No extra significant space -> O(N)
"""
