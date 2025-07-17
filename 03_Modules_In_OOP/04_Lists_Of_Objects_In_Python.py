from random import randint

class Bank:
    def __init__(self):
        self.account = randint(100000, 999999)
        self.full_name = input("Enter your full name: ")
        self.phone_number = input("Enter your phone number: ")
        self.balance = 0
        print(f"\u2705 Account created successfully. Your Account Number is {self.account}")

    def show_info(self):
        print(f"\n--- Account Information ---")
        print(f"Account Number: {self.account}")
        print(f"Full Name     : {self.full_name}")
        print(f"Phone Number  : {self.phone_number}")
        print(f"Balance       : {self.balance} PKR")

    def show_balance(self):
        print(f"Current Balance: {self.balance} PKR")

    def withdraw(self):
        try:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("\u274C Amount must be greater than zero.")
            elif amount > self.balance:
                print("\u274C Insufficient balance.")
            else:
                self.balance -= amount
                print(f"\u2705 Withdrawal successful. Remaining Balance: {self.balance} PKR")
        except ValueError:
            print("\u274C Invalid amount.")

    def deposit(self):
        try:
            amount = int(input("Enter amount to deposit: "))
            if amount <= 0:
                print("\u274C Amount must be greater than zero.")
            else:
                self.balance += amount
                print(f"\u2705 Deposit successful. Current Balance: {self.balance} PKR")
        except ValueError:
            print("\u274C Invalid amount.")


# List to store all Bank accounts
banks = []

def find_account(acc_no):
    for obj in banks:
        if obj.account == acc_no:
            return obj
    return None


# Main menu
while True:
    print("\n========== Bank Menu ==========")
    print("1. Create New Account")
    print("2. Show All Accounts")
    print("3. Deposit Amount")
    print("4. Withdraw Amount")
    print("5. Transfer Amount")
    print("6. Exit")
    print("================================")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("\u274C Invalid input. Please enter a number.")
        continue

    if choice == 1:
        new_account = Bank()
        banks.append(new_account)

    elif choice == 2:
        if not banks:
            print("\u274C No accounts available.")
        else:
            for acc in banks:
                acc.show_info()

    elif choice == 3:
        acc_no = int(input("Enter your account number: "))
        account = find_account(acc_no)
        if account:
            account.deposit()
        else:
            print("\u274C Account not found.")

    elif choice == 4:
        acc_no = int(input("Enter your account number: "))
        account = find_account(acc_no)
        if account:
            account.withdraw()
        else:
            print("\u274C Account not found.")

    elif choice == 5:
        from_acc = int(input("Enter sender's account number: "))
        to_acc = int(input("Enter receiver's account number: "))
        sender = find_account(from_acc)
        receiver = find_account(to_acc)

        if sender and receiver:
            try:
                amount = int(input("Enter amount to transfer: "))
                if amount <= 0:
                    print("\u274C Amount must be greater than zero.")
                elif sender.balance < amount:
                    print("\u274C Insufficient balance in sender's account.")
                else:
                    sender.balance -= amount
                    receiver.balance += amount
                    print("\u2705 Transfer successful.")
                    print(f"Sender Balance: {sender.balance} PKR")
                    print(f"Receiver Balance: {receiver.balance} PKR")
            except ValueError:
                print("\u274C Invalid amount.")
        else:
            print("\u274C One or both account numbers are invalid.")

    elif choice == 6:
        print("\ud83d\udc4b Exiting. Thank you for using our bank system.")
        break

    else:
        print("\u274C Invalid choice. Please select from 1 to 6.")
