import random

class BankAccount:
    account_numbers = set()

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        while True:
            number = str(random.randint(1000000000, 9999999999))
            if number not in BankAccount.account_numbers:
                BankAccount.account_numbers.add(number)
                return number

    def deposit(self, amount):
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