def main():
    manager = AccountManager()

    while True:
        print("\n1. Add Account")
        print("2. Display Accounts")
        print("3. Search Account")
        print("4. Delete Account")
        print("5. Save Accounts")
        print("6. Load Accounts")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Account holder's name: ")
            initial_balance = float(input("Initial balance (default 0): ") or 0)
            account = BankAccount(name, initial_balance)
            manager.add_account(account)
            print("Account added.")

        elif choice == '2':
            manager.display_accounts()

        elif choice == '3':
            account_number = input("Account number: ")
            account = manager.search_account(account_number)
            if account:
                print(f"Holder: {account.get_account_holder()}, Balance: ${account.get_balance():.2f}")
            else:
                print("Account not found.")

        elif choice == '4':
            account_number = input("Account number to delete: ")
            manager.delete_account(account_number)

        elif choice == '5':
            filename = input("Filename to save accounts: ")
            manager.save_to_file(filename)

        elif choice == '6':
            filename = input("Filename to load accounts: ")
            manager.load_from_file(filename)

        elif choice == '7':
            print("Exiting.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()