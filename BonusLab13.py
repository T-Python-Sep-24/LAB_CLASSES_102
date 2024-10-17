#Bonus Lab 13

import pickle
from Lab13 import BankAccount

class AccountManager:
    def __init__(self):
        self.user_accounts = []

#Add Account
    def add_account(self, bank_account: BankAccount):
        self.user_accounts.append(bank_account)
        print("Bank Account Added Successfully.")


#Display Account   
    def display_accounts(self):
        if not self.user_accounts:
            print("No accounts found.")
        for account in self.user_accounts:
            print(account)


#Search Account
    def search_accounts(self, account_number):
        for account in self.user_accounts:
            if account.account_number == account_number:
                print(account)
                return account
            
        else:    
            print("Account is Not Found")
            return None
        

#Delete Account
    def delete_account(self, account_number):
        account = self.search_accounts(account_number)
        if account:
            self.user_accounts.remove(account)
            print("Account Deleted Successfully")

        else:
            print("The Account Could Not be Deleted")


#Save Account with pickle
    def save_account(self, filename:str):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self.user_accounts, file)
                print("Accounts Saved")
        
        except Exception as e:
            print(f"Error Saving File: {e}")


#Load Account with pickle
    def load_account(self, filename: str):
        try:
            with open(filename, 'rb') as file:
                self.user_accounts = pickle.load(file)
                print("Accounts Loaded")
                
        except FileNotFoundError:
            print("File Not Found")
            
        except Exception as e:
            print(f"Error Loading File: {e}")        

