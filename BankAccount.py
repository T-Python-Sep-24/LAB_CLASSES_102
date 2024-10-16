import datetime
import random

class BankAccount():

    used_account_numbers = []  # A temporary list to maintain account numbers that already been assigned to an account.

    def __init__(self, account_holder: str, initial_balance: float = 0):
        """
        This is the constructor/initializer function for the bank account class
        :param account_holder:
        :param initial_balance:
        """
        self.__account_holder = account_holder
        self.__balance = initial_balance  # 0 is the default balance
        self.__account_number = self.generate_account_number()

    def deposit(self, amount: float):
        """
        This function is to deposit amount of money to the account
        :param amount:
        :return: balance
        """
        if amount > 0:
            self.__balance += amount
        else:
            raise "You Cannot deposit less than 0"
        return self.__balance

    def withdraw(self, amount: float):
        """
        This function is to withdraw amount of money from the account
        :param amount:
        :return: balance
        """
        if self.__balance >= amount > 0:
            self.__balance -= amount
        else:
            raise "You have No Sufficient Funds"
        return self.__balance

    def get_balance(self):
        """
        This function is to return the current balance of the account
        :return: balance
        """
        return self.__balance

    def get_account_holder(self):
        """
        This function is to return the account holder's name of the account
        :return: account_holder
        """
        return self.__account_holder

    def get_account_number(self):
        """
        This function is to return the account number of the account
        :return: account_number
        """
        return self.__account_number

    def generate_account_number(self):
        """
        This function is to generate 10 digits unique account number
        :return: account_number
        """
        while True:
            account_number = random.randint(0000000000, 9999999999)  # unique 10 numbers

            if account_number not in BankAccount.used_account_numbers:
                BankAccount.used_account_numbers.append(account_number)
                return account_number


# Testing BankAccount Class
# try:
    # account = BankAccount("Hmzh", 1000)
    # print(f"Account Number: {account.get_account_number()}")
    # print(f"Account Holder: {account.get_account_holder()}")
    # print(f"Initial Balance: {account.get_balance()}")
    # account.deposit(500)
    # print("Balance:", account.get_balance())
    # account.withdraw(300)
    # print("Balance:", account.get_balance())
# except Exception as e:
# print(e)