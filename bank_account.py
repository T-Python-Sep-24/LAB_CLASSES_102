import random
import pickle

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


class AccountManager:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def display_accounts(self):
        for account in self.accounts:
            print(f"Holder: {account.get_account_holder()}, "
                  f"Number: {account.get_account_number()}, "
                  f"Balance: ${account.get_balance():.2f}")

    def search_account(self, account_number):
        return next((account for account in self.accounts if account.get_account_number() == account_number), None)

    def delete_account(self, account_number):
        account = self.search_account(account_number)
        if account:
            self.accounts.remove(account)
            print("Account deleted.")
        else:
            print("Account not found.")

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.accounts, file)
        print("Accounts saved.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.accounts = pickle.load(file)
            print("Accounts loaded.")
        except FileNotFoundError:
            print("File not found.")