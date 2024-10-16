import random
import json
import os
import pickle

class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float):
        self.account_holder = account_holder
        self.__balance = initial_balance
        self.account_number = self.__auto_generate_number()

    def __auto_generate_number(self):
        account_numbers = set()
        if os.path.exists('account_numbers.json'):
            with open('account_numbers.json', 'r') as file:
                account_numbers = set(json.load(file))

        while True:
            number = random.randint(1000000000, 9999999999)
            if number not in account_numbers:
                account_numbers.add(number)
                with open('account_numbers.json', 'w') as file:
                    json.dump(list(account_numbers), file)
                return number

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance: float):
        self.__balance = new_balance

    def get_account_number(self):
        return self.account_number

    def get_account_holder(self):
        return self.account_holder

    def deposit(self, amount: float):
        self.set_balance(amount + self.get_balance())
        return self.get_balance()

    def withdraw(self, amount: float):
        if amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
        else:
            print(f'Sorry {self.get_account_holder()}! The amount {amount} to withdraw exceeds the account balance {self.get_balance()}')
        return self.get_balance()

class AccountManager:
    def __init__(self):
        self.accounts = self.load_from_file('accounts.pkl')

    def add_account(self, bank_account: BankAccount):
        self.accounts[bank_account.get_account_number()] = {
            'account_holder': bank_account.get_account_holder(),
            'balance': bank_account.get_balance(),
        }
        self.save_to_file('accounts.pkl', self.accounts)

    def display_accounts(self):
        i = 0
        for number, account in self.accounts.items():
            print(f'{i}. Account Number: {number}, Account Holder Name: {account["account_holder"]}, Account Balance: {account["balance"]}')
            i += 1

    def search_accounts(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            print(f'Account Found! Account Number: {account_number}, Account Holder Name: {account["account_holder"]}, Account Balance: {account["balance"]}')
            return True
        else:
            print('Account not found!')
            return False

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f'Account Number {account_number} has been deleted.')
            self.save_to_file('accounts.pkl', self.accounts)
            return True
        else:
            print('Account not found!')
            return False

    def save_to_file(self, filename: str, accounts: dict):
        with open(filename, 'wb') as file:
            pickle.dump(accounts, file)

    def load_from_file(self, filename: str):
        if not os.path.exists(filename):
            return {}  
        
        with open(filename, 'rb') as file:
            return pickle.load(file)


# import random
# import json
# import os
# import pickle

# class BankAccount:    
#     def __init__(self, account_holder:str, initial_balance: float):
#         self.account_holder = account_holder
#         self.initial_balance = initial_balance
#         self.__balance = initial_balance
#         self.account_number = self.__auto_generate_number()
    
#     def __auto_generate_number(self):
#         account_numbers = set()
#         if os.path.exists('account_numbers.json'):
#             with open('account_numbers.json', 'r') as file:
#                 account_numbers = set(json.load(file))
            
#         stop = True
#         while stop:
#             number = random.randint(1000000000, 9999999999)
            
#             if number not in account_numbers:
#                 account_numbers.add(number)
#                 stop = False
                
#         with open('account_numbers.json', 'w') as file:
#             json.dump(list(account_numbers), file)
            
#         return number
    
#     def get_balance(self):
#         return self.__balance
    
#     def set_balance(self, newBalance:float):
#         self.__balance = newBalance
        
#     def get_account_number(self):
#         return self.account_number
    
#     def get_account_holder(self):
#         return self.account_holder
    
#     def deposit(self, amount:float):
#         self.set_balance(amount + self.get_balance())
#         return self.get_balance()
    
#     def withdraw(self, amount):
#         if amount <= self.get_balance():
#             self.set_balance(self.get_balance() - amount)
#         else:
#             print(f'Sorry {self.get_account_holder()}! The amount {amount} to withdraw exeeds the account balance {self.get_balance()}')
    
#         return self.get_balance()

# class AccountManager(BankAccount):
#     def __init__(self, account_holder:str, initial_balance: float):
#         super().__init__(account_holder, initial_balance)
        
#     def add_account(self, bank_account: BankAccount):
#         accounts = self.load_from_file('acounts.pkl')
#         accounts[self.get_account_number()] = {
#             'account_holder': self.get_account_holder,
#             'balance': self.get_balance,
#         }
#         self.save_to_file('acounts.pkl', accounts)
    
#     def display_accounts(self):
#         accounts = self.load_from_file('acounts.pkl')
#         i = 0
#         for number, account in accounts.items():
#             print(f'{i}. Account Number: {number}, Account Holder Name: {account['account_holder']}, Account Balance: {account['balance']}')
#             i += 1
            
#     def search_accounts(self, account_number):
#         accounts = self.load_from_file('acounts.pkl')
#         if account_number in accounts:
#             print('Account Found!')
#             print(f'Account Number: {account_number}, Account Holder Name: {accounts[account_number]['account_holder']}, Account Balance: {accounts[account_number]['balance']}')
#             return True
#         else:
#             print('Account not found!')
#             return False
        
#     def delete_account(self, account_number):
#         accounts = self.load_from_file('acounts.pkl')
#         if account_number in accounts:
#             del accounts[account_number]
#             print(f'Account Number {account_number} Has been deleted:')
#             return True
#         else:
#             print('Account not found!')
#             return False
    
#     def save_to_file(self, filename: str, accounts:dict):
#         with open(filename, 'wb') as file:  
#             pickle.dump(accounts, file)
#         file.close()
    
#     def load_from_file(self, filename: str):
#         with open(filename, 'rb') as file:
#             accounts = pickle.load(file)
#         file.close() 
        
#         return accounts
                
            