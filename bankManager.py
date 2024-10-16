from bankAccount import *
import pickle
class AccountManager:
   def __init__(self):
       self.accounts = []

   def add_account(self, bank_account: BankAccount):
       self.accounts.append(bank_account)

   def display_accounts(self):
       for account in self.accounts:
           print(account)

   def search_accounts(self, account_number):
       for account in self.accounts:
           if account.get_account_number() == account_number:
               return account
       print("Account not found.")
       return None

   def delete_account(self, account_number):
       account = self.search_accounts(account_number)
       if account:
           self.accounts.remove(account)
           print(f"Account {account_number} deleted.")

   def save_to_file(self, filename: str):
       with open(filename, 'wb') as file:
           pickle.dump(self.accounts, file)
           print("Accounts saved to file.")

   def load_from_file(self, filename: str):
       try:
           with open(filename, 'rb') as file:
               self.accounts = pickle.load(file)
               print("Accounts loaded from file.")
       except FileNotFoundError:
           print("File not found.")
       except Exception as e:
           print(f"An error occurred: {e}")
