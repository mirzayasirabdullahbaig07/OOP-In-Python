from random import randint

class Bank:
    def __init__(self) -> None:
        self.account = randint(100000, 999999)
        self.full_name = input("Enter the name = ")
        self.phone_number = int(input("Enter phone number = "))
        self.balance = 0

    def show_info(self):
        print(f"\nAccount Number = {self.account}")
        print(f"User Name      = {self.full_name}")
        print(f"Phone Number   = {self.phone_number}")
        print(f"Balance        = {self.balance}\n")

    def show_balance(self):
        print(f"Current Balance = {self.balance}")

    def withdraw(self) -> None:
        amount = int(input("Enter amount to withdraw = "))
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount

    def deposit(self):
        amount = int(input("Enter amount to deposit = "))
        self.balance += amount


# List to store Bank objects
Banks = []

while True:
    print("\n--- Bank Menu ---")
    print("1. Create User Account")
    print("2. Show All Details")
    print("3. Deposit")
    print("4. Exit")

    choice = int(input("Enter choice = "))

    if choice == 1:
        obj = Bank()
        Banks.append(obj)

    elif choice == 2:
        if len(Banks) == 0:
            print("No account is created yet.")
        else:
            for account in Banks:
                account.show_info()

    elif choice == 3:
        if len(Banks) == 0:
            print("No account is created yet.")
        else:
            acc_no = int(input("Enter your account number = "))
            for obj in Banks:
                if obj.account == acc_no:
                    obj.deposit()
                    break
            else:
                print("Account not found.")

    elif choice == 4:
        break

    else:
        print("Invalid choice. Check your input.")
