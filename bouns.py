import pickle
from LAB_BankAccount import BankAccount

class AccountManager:
    
    def __init__(self) -> None:
        
        self.accounts = []  

    def add_account(self, bank_account: BankAccount):
        self.accounts.append(bank_account)

    def display_accounts(self):
        if not self.accounts:
            print("no accounts found.")
        else:
            for account in self.accounts:
                print(account) 

    def search_accounts(self, account_number):
        found = False
        for account in self.accounts:
            if account.get_account_number() == account_number:
                print(f"account found: {account}")
                found = True
                break  
        if not found:
            print("account not found.")

    def delete_account(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                self.accounts.remove(account)
                print("account deleted.")
                return
        print("account not found")

    def save_to_file(self, filename: str): 
        with open(filename, 'wb') as file:
            pickle.dump(self.accounts, file)
        print("accounts saved to file.")

    def load_from_file(self, filename: str):
        try:
            with open(filename, 'rb') as file:
                self.accounts = pickle.load(file)
            print("accounts loaded from file.")
        except FileNotFoundError:
            print("file not found.")
        except Exception as e:
            print(f"error loading accounts: {e}") 


def main():
    manager = AccountManager()
    options = '''
     1. add Bank account
     2. aisplay accounts
     3. search account
     4. delete account
     5. save accounts
     6. load accounts
     7. exit
     '''
    try:
        while True:
            print(options)
            selection = input("choose an option: ")

            if selection == '1':
                holder = str(input("enter account holder name: "))
                balance = float(input("enter balance: ") or 0)
                account = BankAccount(holder, balance)
                manager.add_account(account)

            elif selection == '2':
                manager.display_accounts()

            elif selection == '3':
                account_number = input("enter account number : ")
                manager.search_accounts(account_number)

            elif selection == '4':
                account_number = input("Enter account number : ")
                manager.delete_account(account_number)

            elif selection == '5':
                manager.save_to_file("allaccounts.pkl")

            elif selection == '6':
                manager.load_from_file("allaccounts.pkl")

            elif selection == '7':
                print("exiting program")
                break
            else:
                print("invalid option. try again")
    except ValueError:
        print("enter a vild number")
        
main()
