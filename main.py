from BankClasses import BankAccount

ac1 = BankAccount("Areej",100)
ac2 = BankAccount("Reem")
print(f"Bank account of ({ac1.get_account_holder()}) and its number is: {ac1.get_account_number()} has {ac1.get_balance()} SR ")
print(f"Bank account of ({ac2.get_account_holder()}) and its number is: {ac2.get_account_number()} has {ac2.get_balance()} SR ")

print(ac2.deposit(100))
print(ac1.withdraw(50))
print(ac1.withdraw(100))
print(ac1.get_balance())






