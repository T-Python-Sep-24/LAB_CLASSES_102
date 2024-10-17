import random

class BankAccount:
    id_acc = 1000000100
    def __init__(self, name, initial_balance: int = 0):

        self.name = name
        self.initial_balance = initial_balance
        self.account_number=BankAccount.id_acc
        BankAccount.id_acc+= 11

    def deposit(self, a):
        self.initial_balance += a
        return self.initial_balance

    def withdraw(self, w):
        if w > self.initial_balance:
            print("sorry your balance not that much as you know")
        else:
            self.initial_balance -= w
        return self.initial_balance

    def get_balance(self):
        return self.initial_balance

    def get_account_holder(self):
        return self.name

    def get_account_number(self):
        return self.account_number


prson1 = BankAccount("saleh", 200)
print(prson1.deposit(200))
prson1.withdraw(500)
print(prson1.get_balance())
print(prson1.get_account_number())
prson2 = BankAccount("Saud")
print(prson2.get_balance())
print(prson2.get_account_number())

