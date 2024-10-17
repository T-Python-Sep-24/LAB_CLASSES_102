from classes import BankAccount, AccountsData

# creat instance of AccountsData
accounts_data = AccountsData()

# create instance of BankAccount
ahmedAccount = BankAccount("Ahmed", accounts_data, 1000)

# call object methods
print(f"Account holder: {ahmedAccount.get_account_holder()}")
print(f"Account number: {ahmedAccount.get_account_number()}")
print(f"Balance: {ahmedAccount.get_balance()}")
ahmedAccount.deposit(500)
ahmedAccount.withdraw(300)
