import random


class BankAccount:
    _account_numbers = set()
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        while True:
            number = str(random.randint(1000000000, 9999999999))
            if number not in BankAccount._account_numbers:
                BankAccount._account_numbers.add(number)
                return number

    def deposit(self, amount):
        self.balance = self.balance+ amount
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return amount
    def get_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.account_holder

    def get_account_number(self):
        return self.account_number


