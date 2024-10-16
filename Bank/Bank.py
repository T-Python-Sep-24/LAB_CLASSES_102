import random
class BankAccount:
    account=set()
    def __init__(self,account_holder:str,account_balance:float=0) -> None:
        self.account_holder=account_holder
        self.__set_balance(account_balance)
        self.set_accountnumber()
    def __set_balance(self,account_balance):
        if account_balance>0:
            self.__account_balance=account_balance
        else:
            raise ValueError(" must be posotive ammount")
            
    
    def set_accountnumber(self):
        while True:
            self.__account_number=random.randint(1000000000,9999999999)
            if self.__account_number not in self.account:
               self.account.add(self.__account_number)
               break

    def get_balance(self)->float:
        return self.__account_balance
    
    def get_accountnumber(self):
        return int(self.__account_number)
    
    def get_accountholder(self):
        return self.account_holder
    
    def deposit(self,ammount:float):
        balance=self.get_balance()
        if ammount>0:
            new_balance =balance+ammount
            self.__set_balance(new_balance)
            print(f"Balance now : {self.get_balance()}")
        else:
            raise ValueError("the ammount must be a float value and not negative")
        

    def withdraw(self,ammount:float):
        balance=self.get_balance()
        if ammount<=balance and ammount>0:
            new_balance= balance-ammount
            self.__set_balance(new_balance)
            print(f"Balance now : {self.get_balance()}")
        else:
            raise ValueError("insufficient ammount your trying to withdraw")