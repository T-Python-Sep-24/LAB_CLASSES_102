from Bank.Bank_account import BankAccount
from Bank.Account_manager import AccountManager

def main():
    manager = AccountManager()
    filename = "accounts_data.pkl"

    manager.load_from_file(filename)

    while True:
        print("\n--- Bank Account Manager ---")
        print("1. Add a new account")
        print("2. Display all accounts")
        print("3. Search for an account")
        print("4. Delete an account")
        print("5. Save accounts to file")
        print("6. Load accounts from file")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice (1-7): "))
            if choice == 1:
                name = input("Enter account holder's name: ")
                balance = float(input("Enter initial balance: "))
                new_account = BankAccount(name, balance)
                manager.add_account(new_account)
            elif choice == 2:
                manager.display_accounts()
            elif choice == 3:
                account_number = input("Enter account number to search: ")
                account = manager.search_accounts(account_number)
                if account:
                    print(account)
                else:
                    print("Account not found.")
            elif choice == 4:
                account_number = input("Enter account number to delete: ")
                manager.delete_account(account_number)
            elif choice == 5:
                manager.save_to_file(filename)
            elif choice == 6:
                manager.load_from_file(filename)
            elif choice == 7:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
