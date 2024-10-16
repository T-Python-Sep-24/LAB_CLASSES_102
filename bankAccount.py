class BankAccount:
   account_counter = 0

   def __init__(self, account_holder, initial_balance=0):
       BankAccount.account_counter += 1
       self.account_holder = account_holder
       self.balance = initial_balance
       self.account_number = 1000000000 + BankAccount.account_counter

   def deposit(self, amount):
       if amount > 0:
           self.balance += amount
           return self.balance
       else:
           print("deposit must be positive")
           return None

   def withdraw(self, amount):
       if amount <= self.balance:
           self.balance -= amount
           return self.balance
       else:
           print("insufficient funds")
           return None

   def get_balance(self):
       return self.balance

   def get_account_holder(self):
       return self.account_holder

   def get_account_number(self):
       return self.account_number
   def __str__(self):
       return f"account holder: {self.account_holder} account number: {self.account_number} balance : {self.balance}"