import random
import os


class BankAccount():
    number_list = []

    def __init__(self, account_holder:str, balance= 0) -> None:
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = self.__account_number()

    @classmethod
    def load_numbers(cls, filename: str):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                for line in file:
                    cls.number_list.append(int(line.strip()))
        else:
            open(filename, 'w').close()

    @classmethod
    def save_numbers(cls, filename: str):
        with open(filename, 'w') as file:
            for number in cls.number_list:
                file.write(f"{number}\n")


    def __account_number(self):
        
        while True:
            random_account_number = random.randint(1000000000, 9999999999)
            if random_account_number not in BankAccount.number_list:
                BankAccount.number_list.append(random_account_number)
                return random_account_number
            




    def deposit(self, amount:int):
        #self.account_holder = input("enter account name: ")
        #self.account_number = input("enter account number:")
        #if self.account_number in BankAccount.number_list:
            #amount = input("enter amount to deposit: ")
        self.balance += amount
            #return (f"account balance {self.balance}")
        #else:
            #print("account not found")


    def withdraw(self, amount):
        #self.account_holder = input("enter account name: ")
        #self.account_number = input("enter account number:")  
        #if self.account_number in BankAccount.number_list:
            #amount = input("enter amount to deposit: ")      
            #if amount <= self.balance:
            
        self.balance -= amount
                #return (f"account balance: {self.balance}")
            #else:
                #print("balance is not enough")


    def get_balance(self):
        print(f"current balance: {self.balance}")


    def get_account_holder(self):
        print(f"account holder name is: {self.account_holder}")
    

    def get_account_number(self):
        print(f"account number is: {self.account_number}")
    
    def __str__(self):
        return f"Account holder: {self.account_holder}, Account number: {self.account_number}, Balance: {self.balance}"


    def save_file(self, filename: str):
        with open(filename, 'a') as file:  
            file.write(f"{self.account_holder},{self.account_number},{self.balance}\n")