import os.path
import pickle
from BankAccount import BankAccount

class AccountManager():

    fileName = 'bank_accounts.pkl'
    def __init__(self):
        self.accounts = []

    def add_account(self, bankAccount: BankAccount):

        self.accounts.append(bankAccount)
        print(f"Account {bankAccount.get_account_number()} added successfully, For Customer: {bankAccount.get_account_holder()} with balancce {bankAccount.get_account_holder()}")
        self.save_to_file(self.fileName)

    def display_accounts(self):

        self.load_from_file(self.fileName)
        for i in self.accounts:
            print(i.get_account_holder())

    def search_accounts(self, account_number):
        pass
    def delete_account(self, account_number):
        pass


    def save_to_file(self, fileName):
        with open(fileName, 'wb') as f:  # open a text file
            pickle.dump(self.accounts, f) # serialize the list


    def load_from_file(self, fileName):
        
        try:
            with open(fileName, 'rb') as file:
                self.accounts = pickle.load(file)
                print(f"Accounts loaded from {fileName}.")
                return self.accounts
        except Exception as e:
            print(f"Error loading from file: {e}")
