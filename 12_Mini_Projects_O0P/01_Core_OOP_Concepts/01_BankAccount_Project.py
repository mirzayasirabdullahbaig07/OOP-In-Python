"""
OOP Mini Project Number 1
Category: Core OOP Concepts

# 1. Create a BankAccount class with deposit, withdraw, and balance methods

Problem Statement:
------------------
We need to create a BankAccount class that:
1. Stores account details like account_holder and balance.
2. Allows depositing money into the account.
3. Allows withdrawing money (only if there is enough balance).
4. Allows checking the current balance.

This project demonstrates:
- Class design
- Encapsulation
- Input validation
- Testing using __main__
"""

# -------------------- CLASS DEFINITION --------------------

class BankAccount:
    """A simple bank account class."""

    def __init__(self, account_holder, balance=0):
        """
        Initialize account with:
        - account_holder: The name of the account owner
        - balance: Starting balance (default is 0)
        """
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit money into account.
        - Only positive amounts are allowed.
        - Adds the amount to current balance.
        """
        if amount <= 0:
            print(" Deposit amount must be positive.")
            return self.balance
        self.balance += amount
        print(f" Deposited {amount}. New Balance = {self.balance}")
        return self.balance

    def withdraw(self, amount):
        """
        Withdraw money from account.
        - Only positive amounts are allowed.
        - You cannot withdraw more money than you have.
        """
        if amount <= 0:
            print(" Withdrawal amount must be positive.")
            return self.balance
        if amount > self.balance:
            print(" Insufficient balance.")
            return self.balance
        self.balance -= amount
        print(f" Withdrew {amount}. New Balance = {self.balance}")
        return self.balance

    def check_balance(self):
        """Display the current balance."""
        print(f" Account Holder: {self.account_holder}, Current Balance = {self.balance}")
        return self.balance

    def __str__(self):
        """Readable string when printing the object."""
        return f"Account Holder: {self.account_holder}, Balance: {self.balance}"


# -------------------- TESTING SECTION --------------------

if __name__ == "__main__":
    # Create a bank account for Yasir with starting balance 100000
    account1 = BankAccount("Yasir", 100000)
    print(account1)   # Calls __str__

    # Check balance
    account1.check_balance()

    # Deposit 500
    account1.deposit(500)

    # Try to withdraw more money than balance
    account1.withdraw(200000)

    # Try to withdraw a negative amount
    account1.withdraw(-100)

    # Deposit a negative amount
    account1.deposit(-300)

    # Withdraw a valid amount
    account1.withdraw(2000)

    # Final balance check
    account1.check_balance()
