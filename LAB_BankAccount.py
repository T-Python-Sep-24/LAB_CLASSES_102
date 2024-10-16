
import random
class  BankAccount: 
    unique_account_numbers = []

    def __init__(self,account_holder:str,initial_balance:float = 0) -> None:
        self.account_holder = account_holder
        self.balance =  initial_balance if initial_balance >= 0 else 0
        self.account_number = self.__generated_number()

    def __generated_number(self):
        while True :
            account_number = str(random.randint(1000000000,9999999999))
            if account_number not in BankAccount.unique_account_numbers:
                BankAccount.unique_account_numbers.append(account_number)
                return account_number
    def __repr__(self):
        return f"account holder: {self.account_holder}, account number: {self.account_number}, balance: {self.balance}"
    
    
    def deposit(self, amount):
        if  amount > 0 :
            self.balance += amount
            return f" {amount} has been added . new balance : {self.balance}"
        else:
            return f"you must specify a valid amount for the deposit"
            
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return self.balance   
        else:
            print("you must specify a valid amount for the withdrawal")
            return self.balance
        

    def get_balance(self):
        return f"current balance {self.balance}"
    
    def get_account_holder(self):
        return self.account_holder
    
    def get_account_number(self):
       return self.account_number
    
    









    