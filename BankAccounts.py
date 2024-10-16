import random
import os
import pickle

class BankAccount():
    number_list = []

    def __init__(self, account_holder:str, balance= 0) -> None:
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = self.__account_number()
        


    @classmethod
    def save_acc_list(self, filename: str):
        """saves the account numbers to a file"""
        with open(filename, 'w') as file:  
            for account_number in self.number_list:
                file.write(f"{account_number}\n")  


    @classmethod
    def load_from_file(self, filename: str):
        """loads account numbers from a file into number_list using this list to check for repeated account number"""
        self.number_list = []  
        with open(filename, 'r') as file:
            for line in file:
                account_number = int(line.strip())  
                if account_number not in self.number_list:  
                    self.number_list.append(account_number)
    


    def __account_number(self):
        """this function is used to generate account numebrs
    """
        
        while True:
            random_account_number = random.randint(1000000000, 9999999999)
            if random_account_number not in BankAccount.number_list:
                BankAccount.number_list.append(random_account_number)
                return random_account_number
            




    def deposit(self, amount:int):
        self.balance += amount


    def withdraw(self, amount):
            
        self.balance -= amount


    def get_balance(self):
        print(f"current balance: {self.balance}")


    def get_account_holder(self):
        print(f"account holder name is: {self.account_holder}")
    

    def get_account_number(self):
        print(f"account number is: {self.account_number}")
    
    def __str__(self):
        """this function is used to format objects
    """
        return f"Account holder: {self.account_holder}, Account number: {self.account_number}, Balance: {self.balance}"


    def save_to_file(self, filename: str):
        """this function is used to save accounts to txt file
    """
        with open(filename, 'a') as file:  
            file.write(f"{self.account_holder},{self.account_number},{self.balance}\n")


    @classmethod
    def load_file(self, filename: str):
        accounts = []
        with open(filename, 'r') as file:
            for line in file:  
                account_holder, account_number, balance = line.strip().split(',')  
                account = BankAccount(account_holder, int(balance))  
                account.account_number = int(account_number)  
                accounts.append(account)  
        return accounts 
    
        

class AccountManager(BankAccount):
    filename = 'Bank_Accounts.pkl'
    def __init__(self, filename) -> None:
        self.filename = filename
        if not os.path.exists(self.filename):
            self.accounts = []  
            self.save_to_pickle()  
        else:
            self.accounts = self.load_from_pickle()
        
    
    def add_account(self, bank_account: BankAccount =None):
        """this function is used to add account to pkl file
    """
        account_holder = input("enter account holder name: ")
        balance = input("enter balance for account: ")
        bank_account = BankAccount(account_holder, balance)
        
        self.accounts.append(bank_account)
        bank_account.save_to_file(self.filename)

    
    def display_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        for account in self.accounts:
            print(account)
    

    def search_accounts(self):
        acc_number = input("Enter account number you want to find: ")
        found = False
        for account in self.accounts:
            if account.account_number == int(acc_number):  
                print(account)
                found = True
                break
    
        if not found:
            print("Account not found.")
    

    def delete_account(self, account_number = 0):
        
        acc_number = input("enter account number you want to delete: ")
        acc_del = None
        for account in self.accounts:
            if account.account_number == int(acc_number):
                acc_del = account
                break
        if acc_del:
            self.accounts.remove(acc_del)
            self.save_to_pickle()
        else:
            print("account not found")
   
    def save_to_pickle(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.accounts, file)

    def load_from_pickle(self):
        try:
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        except (EOFError, FileNotFoundError):
            return []





    