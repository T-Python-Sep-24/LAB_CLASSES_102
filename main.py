from classes1 import BankAccount



account = BankAccount("Eyad", 0)

print(f"Account Holder: {account.get_account_holder()}")
print(f"Account Number: {account.get_account_number()}")
print(f"Initial Balance: {account.get_balance()}")

account.deposit(500)
print(f"Balance: {account.get_balance()}")

account.withdraw(400)
print(f"Balance: {account.get_balance()}")

account.withdraw(1500)
print(f"Balance: {account.get_balance()}")




