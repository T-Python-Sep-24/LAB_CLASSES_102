import random

class BankAccount:

    used_account_numbers = set()

    def __init__(self, account_holder, initial_balance=0):
        self._account_holder = account_holder
        self._balance = initial_balance
        self._account_number = self._generate_account_number()

    def _generate_account_number(self):
        while True:
            account_number = random.randint(1000000000, 9999999999)
            if account_number not in BankAccount.used_account_numbers:
                BankAccount.used_account_numbers.add(account_number)
                return account_number

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds.")
        return self._balance

    def get_balance(self):
        return self._balance

    def get_account_holder(self):
        return self._account_holder

    def get_account_number(self):
        return self._account_number
    

