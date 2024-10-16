import random

class BankAccount:
    existing_account_numbers = set()

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = self.generate_unique_account_number()

    def generate_unique_account_number(self):
        while True:
            account_number = str(random.randint(1000000000, 9999999999))
            if account_number not in BankAccount.existing_account_numbers:
                BankAccount.existing_account_numbers.add(account_number)
                return account_number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            print("Deposit amount must be positive.")
            return self.balance

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return self.balance
            else:
                print("Insufficient funds.")
                return self.balance
        else:
            print("Withdrawal amount must be positive.")
            return self.balance

    def get_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.account_holder

    def get_account_number(self):
        return self.account_number

# Example usage
if __name__ == "__main__":
    account = BankAccount("Alice", 100)
    print(f"Account Holder: {account.get_account_holder()}")
    print(f"Account Number: {account.get_account_number()}")
    print(f"Initial Balance: {account.get_balance()}")

    account.deposit(50)
    print(f"Balance after deposit: {account.get_balance()}")

    account.withdraw(30)
    print(f"Balance after withdrawal: {account.get_balance()}")

    account.withdraw(150)  # Attempting to withdraw more than the balance
