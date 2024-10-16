import datetime
import random

# import pickle

class BankAccount():


    def __init__(self, account_holder:str, initial_balance:int = 0):

        self.__account_holder = account_holder
        self.__initial_balance = initial_balance  # 0 is the default balance
        self.__account_number = self.get_account_number()

    def deposit(self, amount: int):

        balance = self.get_balance()
        newBalance = balance + amount
        self.set_Balance(newBalance)
        return f"Balance is : {self.get_balance()}, Updated {datetime.datetime.now()}"

    def withdraw(self, amount: int):
        if self.__initial_balance >= amount:
            self.__initial_balance -= amount
        else:
            raise "You have No Sufficient Funds"
        return f" Withdrawing... Balance is : {self.__initial_balance}, Updated {datetime.datetime.now()}"

    def get_balance(self):
        return self.__initial_balance

    def set_Balance(self, newBalance):
        self.__initial_balance = newBalance

    def get_account_holder(self):
        return self.__account_holder
    def get_account_number(self):

        acc_num = random.randint(0000000000, 9999999999)  # unique 10 numbers

        return acc_num

