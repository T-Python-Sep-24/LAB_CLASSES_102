import random

class BankAccount:
    def __init__(self,account_holder:str,initial_balance:float)-> None:
        self.__account_holder=account_holder
        self.__account_num=self.generate_acc_num()
        if initial_balance==None:
            self.initial_balance=0
        else:
            self.initial_balance=initial_balance
    def generate_acc_num(self):
        acc_num=''.join(str(random.sample(range(10),1)[0]) for _ in range(10))
        return acc_num
    def deposit(self, amount:float):
        self.initial_balance+=amount
        return f"updated balance = {self.initial_balance} "
    def withdraw(self,amount:float):
        if amount<0:
            print("The amount must be postive")
        else:
            if amount<=self.initial_balance:
                self.initial_balance=amount
                return self.initial_balance
            else:
                print(f"Error{self.initial_balance}")
                return self.initial_balance
    def set_acc_h(self,account_holder):
        return self.__account_holder==account_holder
    def get_balance(self):
        return self.initial_balance
    def get_account_holder(self):
        return self.__account_holder
    def set_acc_num(self):
        return self.__account_num==self.generate_acc_num()
    def get_account_number(self):
        return self.__account_num