import random
class BankAccount:
    __existing_account_numbers = set()

    def __init__(self, account_holder:str, initial_balance:int = 0 ):
        self.__account_holder = account_holder
        self.__balance = initial_balance
        self.__account_number = self.__generate_unique_account_number()

    def __generate_unique_account_number(self):
        """ generate a unique 10-digit account number."""
        #while True:                 
        account_number = ''.join([str(random.randint(0, 9)) for n in range(10)])
        if account_number not in self.__existing_account_numbers:
                self.__existing_account_numbers.add(account_number)
                return account_number
        
    def deposit(self, amount):
         """Method to deposit money into the account and return updated balance."""

         if amount > 0:
              self.__balance += amount
              return self.__balance
         else :
              raise ValueError("Deposit amount must be greater than zero and positive.")
    
    def withdraw(self, amount):
        """Method to withdraw money from the account, returns updated balance."""
        if  amount > 0 and self.__balance >= amount:
           self.__balance -= amount
           return self.__balance
        else:
             raise ValueError("The balance is insufficient to complete the transaction")
    def get_balance(self):
         return self.__balance
    
    def get_account_holder(self):
         return self.__account_holder
    
    def get_account_number(self):
         return self.__account_number
    

