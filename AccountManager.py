import os.path
import pickle
from BankAccount import *

class AccountManager():

    bankAccounts = []

    # def __init__(self, bankAccount: BankAccount, fileName='bank_accounts.pkl'):
    #     self.bankAccount = bankAccount
    #     self.fileName = fileName

    def add_account(self, bankAccount: BankAccount):
        acc = {
            "acc_holder": bankAccount.get_account_holder(),
            "acc_balance": bankAccount.get_balance(),
            "acc_number": bankAccount.get_account_number()
        }
        self.bankAccounts.append(acc)
        self.save_to_file(self.fileName)
        print(f"Account {self.bankAccount.get_account_number()} added successfully, For Customer: {self.bankAccount.get_account_holder()} with balancce {self.bankAccount.get_account_holder()}")
    def display_accounts(self):
        print(self.load_from_file(self.fileName))
    def search_accounts(self, account_number):
        pass
    def delete_account(self, account_number):
        pass


    def save_to_file(self, fileName):
        with open(fileName, 'wb') as f:  # open a text file
            pickle.dump(self.bankAccounts, f) # serialize the list


    def load_from_file(self, fileName):
        with open(fileName, 'wb', encoding="utf-8") as f:  # open a text file
            if os.path.getsize(fileName) > 0:

                x = pickle.load(f)  # serialize the list
                print(x)
            else:
                print("no account Yet")

