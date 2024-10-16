import random
class BankAccount:
    
    def __init__(self,account_holder:str,initial_balance:float=0) -> None:
        self.set_account_holder(account_holder)
        self.set_balance(initial_balance)
        self.set_account_number()
    
    # set methods
    def set_account_holder(self, account_holder):
        if not isinstance(account_holder, str):
            raise Exception("Account holder name should be a string")
        self.__account_holder = account_holder        
    
    def set_account_number(self):
        account_number=""
        for n in range(10):
            n=random.randint(0,9)
            account_number+=str(n)
        self.__account_number=account_number

    def set_balance(self,current_balance):
        if not isinstance(current_balance,(int,float)):
            raise Exception("balance should be a number")
        self.__current_balance=current_balance
    
    # get methods
    def get_account_holder(self):
        return self.__account_holder
    
    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__current_balance
    

    # methods
    def deposit(self,amount):
       original=self.get_balance()
       updated_balance=original+amount
       self.set_balance(updated_balance)
       return f"Successful deposit: {amount} SR to account: {self.get_account_number()}. \nTotal: {self.get_balance()}"



    def withdraw(self,amount):
       original=self.get_balance()
       updated_balance=original-amount
       if updated_balance < 0:
           return f"there is no enough money to compelte your process"
       self.set_balance(updated_balance)
       return f"Successful withdraw: {amount} SR from account: {self.get_account_number()}. \nTotal: {self.get_balance()}"
