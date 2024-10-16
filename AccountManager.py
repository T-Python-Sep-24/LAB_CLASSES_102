import os.path
import pickle
from BankAccount import BankAccount

class AccountManager():

    fileName = 'bank_accounts.pkl'
    def __init__(self):
        self.accounts = []

    def add_account(self, bankAccount: BankAccount):
        try:
            self.accounts.append(bankAccount)
            print(f" >>> ✅ Account {bankAccount.get_account_number()} ADDED SUCCESSFULLY , "
                  f"For Customer: {bankAccount.get_account_holder()} "
                  f"With balancce {bankAccount.get_account_holder()}")
            self.save_to_file(self.fileName)
        except Exception as e:
            print(e)

    def display_accounts(self):
        try:
            self.load_from_file(self.fileName)
            print(" --------- Accounts ---------")
            for i, account in enumerate(self.accounts, start=1):
                print(f"{i}. Account {account.get_account_number()}, "
                      f"For Customer: {account.get_account_holder()} "
                      f"With balancce {account.get_account_holder()}")
            print(" --------- -------- ---------")
        except Exception as e:
            print(e)
    def search_accounts(self, account_number):

        try:
            accounts = self.load_from_file(self.fileName)

            print(" --------- Accounts Founded ---------")
            for i, account in enumerate(accounts, start=1):
                if int(account.get_account_number()) == int(account_number):
                    print(f"{i}. Account number: {account.get_account_number()} "
                          f"for Customer {account.get_account_holder()} "
                          f"Have the balance {account.get_balance()}")
                else:
                    print("No match")
            print(" --------- -------- -------- ---------")

        except Exception as e:
            print(e)

    def delete_account(self, account_number):

        accounts = self.load_from_file(self.fileName)
        for i, account in enumerate(accounts, start=1):
            if int(account.get_account_number()) == int(account_number):
                self.accounts.remove(account)
                print("Account Deleted Successfully ✅")
                self.save_to_file(self.fileName)
            else:
                print("No match")

        # for i in accounts:
        #     print(i.get_account_number())

    def save_to_file(self, fileName):
        try:
            with open(fileName, 'wb') as f:
                pickle.dump(self.accounts, f)
        except Exception as e:
            print(e)

    def load_from_file(self, fileName):
        
        try:
            with open(fileName, 'rb') as file:
                self.accounts = pickle.load(file)
                print(f"Accounts loaded from {fileName}.")
                return self.accounts
        except Exception as e:
            print(f"Error loading from file The File is Empty: {e}")
