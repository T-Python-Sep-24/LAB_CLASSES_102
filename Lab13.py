# Lab 13

import random

class BankAccount:

    exisit_account = set()

    def __init__(self, account_holder:str, initial_balance:float = 0.0):
        #Attributes
        self.account_holder = account_holder
        self.account_number = self.generate_acount_numbers()
        self.initial_balance = initial_balance

    #Genrate Random Numbers
    def generate_acount_numbers(self):
        while True:
            account_number = random.randint(10**9, 10**10 -1)
            if account_number not in BankAccount.exisit_account:
                BankAccount.exisit_account.add(account_number)
                return account_number
          


#Methods

#No.1
    def deposit(self):
        amount = float(input("Please Enter the Amount You Would Like to Add to Your Account: "))
        self.initial_balance += amount
        print (f"You Have Add {amount} into Your Account. Your Balance Now is {self.initial_balance}.")


#No.2
    def withdraw(self):
        amount2 = float(input("Please Enter the Amount You Would Like to Withdrew from Your Account: "))
        if self.initial_balance >= amount2:
            self.initial_balance -= amount2
            print(f"You Have Withdrew {amount2} from Your Account. Your Balance Now is {self.initial_balance}.") #Problem

        else:
            print(f"You Don't Have Enough Money to Withdrew the {amount2} You Want.")    


#No.3
    def get_balance(self): 
        print(f"Your Current Balance is: {self.initial_balance}.") 
        return self.initial_balance


#No.4
    def get_account_holder(self):
        print(f"The Name for This Bank Account is: {self.account_holder}.")
        return self.account_holder


#No.5
    def get_account_number(self):
        print(f"Your Account IBN is: {self.account_number}.") 
        return self.account_number




