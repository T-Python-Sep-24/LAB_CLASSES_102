from classes import BankAccount, AccountsData
from bonus_classes import AccountManager

# create instance of AccountData for storing accounts nubmers lists
accounts_data = AccountsData()
# get data from pickle file

# create instance of AccountManager
account_manager = AccountManager(accounts_data)


while True:
    print("Pick: \n" +
          "1: to add a bank account\n"+
          "2: to display bank accounts\n" +
          "3: to search for a bank account\n" +
          "4: to delete a bank account\n" +
          "5: to exit")
    pick: int = input("Enter: ")
    print()

    if pick == "1":
        account_holder = input("Acount holder: ")
        initial_balance = input("Inital balance: ")
        # create instance of BankAccount which will add account number to accounts_data
        bank_account = BankAccount(account_holder, accounts_data, initial_balance)

        # call add account method to add account to the pickle file
        account_manager.add_account(bank_account, accounts_data)
        
    elif pick == "2":
        account_manager.display_accounts(accounts_data)

    elif pick == "3":
        account_number = input("Type the account number: ")
        account_manager.search_accounts(account_number, accounts_data)

    elif pick == "4":
        pass
        account_number = input("Type the account number: ")
        account_manager.delete_account(account_number, accounts_data)

    elif pick == "5":
        pass
        print("Thank you for using the account manager, come back again soon")
        break
    else:
        print("---- Wrong input ----")
        input("")