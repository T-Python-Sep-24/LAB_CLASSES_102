import random
import json
import os
import pickle

class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0):
        self.account_holder = account_holder
        self.__balance = initial_balance
        self.account_number = self.__auto_generate_number()

    def __auto_generate_number(self):
        account_numbers = set()
        if os.path.exists('account_numbers.json'):
            with open('account_numbers.json', 'r') as file:
                account_numbers = set(json.load(file))

        while True:
            number = random.randint(1000000000, 9999999999)
            if number not in account_numbers:
                account_numbers.add(number)
                with open('account_numbers.json', 'w') as file:
                    json.dump(list(account_numbers), file)
                return str(number)

    def deposit(self, amount: float):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount: float):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print(f'Sorry {self.account_holder}! The amount {amount} exceeds the account balance {self.__balance}')
        return self.__balance

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.account_number

    def get_account_holder(self):
        return self.account_holder


class AccountManager:
    def __init__(self):
        self.accounts = self.load_from_file('accounts.pkl')

    def add_account(self, bank_account: BankAccount):
        self.accounts[bank_account.get_account_number()] = {
            'account_holder': bank_account.get_account_holder(),
            'balance': bank_account.get_balance(),
        }
        self.save_to_file('accounts.pkl')

    def display_accounts(self):
        if not self.accounts:
            print("No accounts available.")
            return
        for i, (number, account) in enumerate(self.accounts.items()):
            print(f'{i + 1}. Account Number: {number}, Account Holder: {account["account_holder"]}, Balance: {account["balance"]}')

    def search_accounts(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f'Account Found! Number: {account_number}, Holder: {account["account_holder"]}, Balance: {account["balance"]}')
            return True
        print('Account not found!')
        return False

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            self.save_to_file('accounts.pkl')
            print(f'Account {account_number} deleted.')
            return True
        print('Account not found!')
        return False

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.accounts, file)

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                return pickle.load(file)
        return {}


def main():
    menu = ''' 
1. Add a bank account
2. Display bank accounts
3. Search for a bank account
4. Delete a bank account
5. Deposit
6. Withdraw
7. Exit
'''
    print('Welcome to the Account Manager System!\n')
    manager = AccountManager()

    while True:
        print(menu)
        try:
            choice = int(input('Choose an action: '))
        except ValueError:
            print("Invalid option. Please enter a number.")
            continue

        if choice == 1:
            name = input('Account holder name: ')
            deposit_choice = input('Deposit to new account? (y/n): ').lower()
            balance = float(input('How much to deposit: ')) if deposit_choice == 'y' else 0
            new_account = BankAccount(name, balance)
            manager.add_account(new_account)
            print(f"Account created for {name}. Account Number: {new_account.get_account_number()}")

        elif choice == 2:
            manager.display_accounts()

        elif choice == 3:
            account_number = input('Enter account number to search: ')
            manager.search_accounts(account_number)

        elif choice == 4:
            account_number = input('Enter account number to delete: ')
            manager.delete_account(account_number)

        elif choice == 5:
            account_number = input('Enter account number to deposit into: ')
            if manager.search_accounts(account_number):
                amount = float(input('Amount to deposit: '))
                account = manager.accounts[account_number]
                account_instance = BankAccount(account['account_holder'], account['balance'])
                account_instance.deposit(amount)
                manager.accounts[account_number]['balance'] = account_instance.get_balance()
                manager.save_to_file('accounts.pkl')
                print(f'New balance: {account_instance.get_balance()}')

        elif choice == 6:
            account_number = input('Enter account number to withdraw from: ')
            if manager.search_accounts(account_number):
                amount = float(input('Amount to withdraw: '))
                account = manager.accounts[account_number]
                account_instance = BankAccount(account['account_holder'], account['balance'])
                account_instance.withdraw(amount)
                manager.accounts[account_number]['balance'] = account_instance.get_balance()
                manager.save_to_file('accounts.pkl')
                print(f'New balance: {account_instance.get_balance()}')

        elif choice == 7:
            print("Exiting Account Manager System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
