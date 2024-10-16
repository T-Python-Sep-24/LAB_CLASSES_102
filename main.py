from bankAccount import *
from bankManager import *
def main():
   manager = AccountManager()

   while True:
       print("\nBank Manager Menu:")
       print("1. Add Bank Account")
       print("2. Display Accounts")
       print("3. Search for an Account")
       print("4. Delete an Account")
       print("5. Save Accounts to File")
       print("6. Load Accounts from File")
       print("7. Exit")

       choice = input("Choose an option: ")

       if choice == '1':
           name = input("Enter account holder's name: ")
           balance = float(input("Enter initial balance (default is 0): ") or 0)
           account = BankAccount(name, balance)
           manager.add_account(account)
           print("Account added.")

       elif choice == '2':
           manager.display_accounts()

       elif choice == '3':
           account_number = int(input("Enter account number to search: "))
           account = manager.search_accounts(account_number)
           if account:
               print(account)

       elif choice == '4':
           account_number = int(input("Enter account number to delete: "))
           manager.delete_account(account_number)

       elif choice == '5':
           filename = input("Enter filename to save accounts: ")
           manager.save_to_file(filename)

       elif choice == '6':
           filename = input("Enter filename to load accounts: ")
           manager.load_from_file(filename)

       elif choice == '7':
           print("Exiting program.")
           break

       else:
           print("Invalid option. Please try again.")

if __name__ == "__main__":
   main()
