from bank import BankAccount



if __name__ == "__main__":
    account1 = BankAccount("Mishal", 1000)
    account2 = BankAccount("Basil")

    print(f"Account Holder: {account1.get_account_holder()}")
    print(f"Account Number: {account1.get_account_number()}")
    print(f"Balance: {account1.get_balance()}")
    
    account1.deposit(500)
    print(f"After Deposit, Balance: {account1.get_balance()}")

    account1.withdraw(300)
    print(f"After Withdrawal, Balance: {account1.get_balance()}")

    print(f"Account Holder: {account2.get_account_holder()}")
    print(f"Account Number: {account2.get_account_number()}")
    print(f"Balance: {account2.get_balance()}")
