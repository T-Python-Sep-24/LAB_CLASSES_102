import random

class BankAccount:
    existing_account_numbers = set()

    def __init__(self, account_holder: str, initial_balance: float = 0.0) -> None:
        self.account_holder = account_holder
        self.balance = initial_balance if initial_balance >= 0 else 0.0
        self.account_number = self.generate_account_number()

    def generate_account_number(self) -> str:
        while True:
            account_number = ''.join(random.choices('0123456789', k=10))
            if account_number not in BankAccount.existing_account_numbers:
                BankAccount.existing_account_numbers.add(account_number)
                return account_number

    def deposit(self, amount: float) -> float:
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def get_balance(self) -> float:
        return self.balance

    def get_account_holder(self) -> str:
        return self.account_holder

    def get_account_number(self) -> str:
        return self.account_number