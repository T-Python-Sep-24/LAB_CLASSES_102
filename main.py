from BankAccounts import BankAccount, AccountManager 

BankAccount.load_from_file("bank_accounts_numbers.txt")
BankAccount.load_file("Bank_Accounts.txt")

person1 = BankAccount("fahad", 500)
person2 = BankAccount("ahmed", 200)
print(person1)

person1.deposit( 500)


person1.withdraw(200)


person1.get_balance()


person1.get_account_holder()


person1.get_account_number()


person1.save_to_file("Bank_Accounts.txt")
person2.save_to_file("Bank_Accounts.txt")
BankAccount.save_acc_list("bank_accounts_numbers.txt")



def main():
    """
    this function is used to ask the user to modify bank
    """
    am = AccountManager("Bank_Accounts.pkl")
    while True:
        print("\n1. Add Account")
        print("2. Display Accounts")
        print("3. Search Account")
        print("4. Delete Account")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            am.add_account()
        elif choice == '2':
            am.display_accounts()
        elif choice == '3':
            am.search_accounts()
        elif choice == '4':
            am.delete_account()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")
    am.save_to_pickle()
main()