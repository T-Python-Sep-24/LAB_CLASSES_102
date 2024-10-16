from LAB_BankAccount import BankAccount

def main():
    account1 = BankAccount("alhanouf", 2000)
    account2 = BankAccount("razan")
    print(f"account holder: {account1.get_account_holder()}, account number : {account1.get_account_number()} initial balance : {account1.get_balance()}")
    print(f"account holder: {account2.get_account_holder()}, account number : {account2.get_account_number()} initial balance : {account2.get_balance()}")

    account1.deposit(100)
    print(f"balance after deposit: {account1.get_balance()}")
    account2.deposit(500)
    print(f"balance after deposit: {account2.get_balance()}")

    account1.withdraw(50)
    print(f"balance after withdrawal: {account1.get_balance()}")
    account2.withdraw(100)
    print(f"balance after withdrawal: {account2.get_balance()}")

    account1.withdraw(50000)

    print(account1.get_balance())
    print(account2.get_account_holder())
    print(account2.get_account_number())


main()


