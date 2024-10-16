import random 
class BankAccount :
    def __init__(self , account_holder:str , initial_balance: int  ) :
        self.__account_holder= account_holder
        self.account_number =  random.randint(1000000000, 9999999999)
        self.balance = initial_balance
    
    #Encapsulation
    #Check with spcified attribute    
    def setter(self,account_holder):
        self.__account_holder = account_holder

    def getter(self):
        return self.__account_holder
    
    def deposit (self, amount):
        amount = 0 
        new_balance =  amount + self.balance  
        self.balance = new_balance
        print("is add cach successfully ")
        return f"this is total for {self.balance}"
    
    def withdraw(self ,amount):
        
        if amount >= self.balance and amount <= 0  :
            print("you have in account be required money ")
        
        else: 
            print("it's not required money")

    
    def get_balance(self):
        return f"This is total the balance: {self.balance} for to  user :{self.__account_holder} "
    
    
    def get_account_holder (self):
        return f"This is name: {self.__account_holder}"
    
    
    def get_account_number(self):
        return f"This is number of the account holder : {self.account_number} for to  user :{self.__account_holder}"
    