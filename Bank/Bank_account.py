import random

class BankAccount:
    existing_account_numbers = set()

    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = self._generate_unique_account_number()

    def _generate_unique_account_number(self):
        while True:
            account_number = str(random.randint(1000000000, 9999999999))
            if account_number not in BankAccount.existing_account_numbers:
                BankAccount.existing_account_numbers.add(account_number)
                return account_number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
            return self.balance
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.account_holder

    def get_account_number(self):
        return self.account_number

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Account Number: {self.account_number}, Balance: {self.balance}"
