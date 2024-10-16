from managerClass import AccountManager
from BankClasses import BankAccount
try:
    user=AccountManager()
    while True:
        choice=input('''
    Welcome to Accounts Manager program:
    1- Add account
    2- Display accounts
    3- Search account
    4- Delete account
    0- Exit             
    ''')
        if choice=="1":
            name=input("Enter the name of account holder: ")
            initial_balance=input("Enter the balance: ")
            c_initial_balance=float(initial_balance)
            new_account=BankAccount(name,c_initial_balance)
            user.add_account(new_account)
            print("Account added successfully")
            input("Press Enter to continue >>>")

        elif choice=="2":
            user.display_accounts()
            input("Press Enter to continue >>>")

        elif choice=="3":
            account_number=input("Enter the account number you want to search: ")
            result=user.search_accounts(account_number)
            print(result)
            input("Press Enter to continue >>>")

        elif choice=="4":
            account_number=input("Enter the account number you want to delete: ")
            result=user.delete_account(account_number)
            print(result)
            input("Press Enter to continue >>>")

        elif choice=="0":
            print("Thank you for using our Account Manager program.")
            break

        else:
            print("invalid value. please choose from the menu")
            input("Press Enter to continue >>>")

except Exception as e:
        print(f"Error in the program: {e}")            