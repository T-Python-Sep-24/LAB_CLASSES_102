from BankAccount import BankAccount

account1=BankAccount("Shouq",10000)
account2=BankAccount("Anoud",50000)
account3=BankAccount("Rahaf",100000)
print(account1.withdraw(-500))
print(account2.withdraw(500))
print(account3.withdraw(2500))
print(account1.deposit(600))
print(account1.get_balance())
print(account1.get_account_number())
print(account1.get_account_holder())
