import pickle
from Bank.Bank_account import BankAccount

class AccountManager:
    def __init__(self):
        self.accounts = []

    def add_account(self, bank_account: BankAccount):
        self.accounts.append(bank_account)
        print(f"Account added: {bank_account}")

    def display_accounts(self):
        if not self.accounts:
            print("No accounts to display.")
        else:
            for account in self.accounts:
                print(account)

    def search_accounts(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None

    def delete_account(self, account_number):
        account = self.search_accounts(account_number)
        if account:
            self.accounts.remove(account)
            print(f"Account {account_number} deleted.")
        else:
            print(f"Account {account_number} not found.")

    def save_to_file(self, filename: str):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self.accounts, file)
            print("Accounts saved successfully.")
        except Exception as e:
            print(f"Error saving accounts: {e}")

    def load_from_file(self, filename: str):
        try:
            with open(filename, 'rb') as file:
                self.accounts = pickle.load(file)
            print("Accounts loaded successfully.")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty account list.")
        except Exception as e:
            print(f"Error loading accounts: {e}")
