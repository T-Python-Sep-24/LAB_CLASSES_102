from bank_account import BankAccount

def main():
   
    account = BankAccount("Marwah Adnan", 900.0)
    print(f"Account Holder: {account.get_account_holder()}")
    print(f"Account Number: {account.get_account_number()}")
    print(f"Initial Balance: {account.get_balance()}")

    try:
        account.deposit(50)
        print(f"Balance after deposit: {account.get_balance()}")
    except ValueError as e:
        print(e)

    try:
        account.withdraw(30)
        print(f"Balance after withdrawal: {account.get_balance()}")
    except ValueError as e:
        print(e)

    try:
        account.withdraw(150) 
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()