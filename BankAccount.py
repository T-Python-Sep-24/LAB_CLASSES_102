import datetime
import random

# import pickle

class BankAccount():

    used_acc_nums = []
    def __init__(self, account_holder:str, initial_balance:int = 0):

        self.__account_holder = account_holder
        self.__balance = initial_balance  # 0 is the default balance
        self.__account_number = self.generate_account_number()

    def deposit(self, amount: int):
        if amount > 0:
            self.__balance += amount
        else:
            raise "You Cannot deposit less than 0"
        return self.__balance

    def withdraw(self, amount: int):
        if self.__balance >= amount > 0:
            self.__balance -= amount
        else:
            raise "You have No Sufficient Funds"
        return self.__balance

    def get_balance(self):
        return self.__balance

    def get_account_holder(self):
        return self.__account_holder

    def get_account_number(self):
        return self.__account_number

    def generate_account_number(self):
        while True:
            acc_num = random.randint(0000000000, 9999999999)  # unique 10 numbers

            if acc_num not in BankAccount.used_acc_nums:
                BankAccount.used_acc_nums.append(acc_num)
                return acc_num


# account = BankAccount("John Doe", 1000)
# print(f"Account Number: {account.get_account_number()}")
# print(f"Account Holder: {account.get_account_holder()}")
# print(f"Initial Balance: {account.get_balance()}")
# account.deposit(500)
# print(f"Balance after deposit: {account.get_balance()}")
# account.withdraw(300)
# print(f"Balance after withdrawal: {account.get_balance()}")