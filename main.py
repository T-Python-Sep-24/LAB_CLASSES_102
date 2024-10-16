from BankAccount import BankAccount

def main():
    # Create a bank account for John Doe with an initial balance of 100
    account = BankAccount("John Doe", 100)

    print(f"Account Holder: {account.get_account_holder()}")
    print(f"Account Number: {account.get_account_number()}")
    print(f"Initial Balance: {account.get_balance()}")

    # Deposit money
    new_balance = account.deposit(50)
    print(f"Balance after deposit: {new_balance}")

    # Withdraw money
    new_balance = account.withdraw(30)
    print(f"Balance after withdrawal: {new_balance}")

    # Attempt to withdraw more than the balance
    account.withdraw(150)

if __name__ == "__main__":
    main()
