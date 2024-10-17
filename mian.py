from bank import BankAccount

account1 = BankAccount('Abdullah' , 500)


print(f"Account holder: {account1.get_account_holder()}")
print(f"Account number: {account1.get_account_number()}")
print(f"Initial balance: {account1.get_balance()}")

# Deposit money
account1.deposit(200)
print(f"Balance after deposit: {account1.get_balance()}")

# Withdraw money
account1.withdraw(100)
print(f"Balance after withdrawal: {account1.get_balance()}")

# Try withdrawing more than the balance
#account1.withdraw(700)  # Should print an error message for insufficient funds
print(f"Balance after attempted overdraft: {account1.get_balance()}")

