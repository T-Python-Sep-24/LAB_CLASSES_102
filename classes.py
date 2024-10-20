import random

class BankAccount:
    existing_account_numbers = set()  # Added to store existing account numbers

    def __init__(self, account_holder, initial_balance=0, account_number=None) -> None:
        self.account_holder = account_holder
        self.initial_balance = initial_balance  # Initialize balance here
        self.account_number = account_number

        while True:
            self.account_number = ""
            for _ in range(10):
                self.account_number += random.choice('0123456789')   
            
            if self.account_number not in BankAccount.existing_account_numbers:
                BankAccount.existing_account_numbers.add(self.account_number)
                break

    def deposit(self, amount):
        self.initial_balance += amount
        return amount
    
    def withdraw(self, amount):
        if amount <= self.initial_balance:  
            self.initial_balance -= amount
            return True
        return False
     
    def get_balance(self):
        return self.initial_balance
    
    def get_account_holder(self):
        return self.account_holder

    def get_account_number(self):
        return self.account_number 


account = BankAccount("Account Holder", 0)  


account.deposit(50)  


print(account.get_balance())  

