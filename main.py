from BankAccounts import BankAccount

BankAccount.load_numbers("bank_accounts_numbers.txt")

person1 = BankAccount("fahad", 500)
print(person1)

deposit = person1.deposit( 500)
print(person1)

withdraw = person1.withdraw(200)
print(person1)

person1.get_balance()


person1.get_account_holder()


person1.get_account_number()


person1.save_file("Bank_Accounts.txt")
BankAccount.save_numbers("bank_accounts_numbers.txt")