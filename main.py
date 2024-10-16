import random 
from defienClass import BankAccount 


user1 = BankAccount("Ahmed","100")
user2= BankAccount("Khalid",500)

user1.deposit("1000")
user1.withdraw(50)
print("-"*30)
# View for to user 1  
print(user1.get_account_holder())
print(user1.get_account_number())
print(user1.get_balance())

print("-"*30)
#View for to user 2 
print(user2.get_account_holder())
print(user2.get_account_number())
print(user2.get_balance())

