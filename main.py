from Lab13 import BankAccount
from BonusLab13 import AccountManager

#This is for Bonus Lab 13
def main():

    manager = AccountManager()
    filename = "accounts_data.pkl"
    manager.load_account(filename)

    print("Welcom To Your Bank Account Manager")
    print("*" * 20)

    while True:
        
        user_choice = input("Please Enter Your Choice: \n1. Add New Account \n2. Display All Accounts \n3. Search for an Account \n4. Delete an Account \n5. Save Accounts to File \n6. Load Accounts from File \n7. Exit \n")

        if user_choice == "1":
            name = input("Enter The Name of the Account: ")
            balance = float(input("Enter Initial Balance: "))
            new_account = BankAccount(name, balance)
            manager.add_account(new_account)


        elif user_choice == "2":
            manager.display_accounts()    


        elif user_choice == "3":
            account_number = int(input("Enter The Account Number You Want To Search: "))
            manager.search_accounts(account_number)


        elif user_choice == "4":
            account_number = int(input("Enter The Account Number You Want To Delete: "))
            manager.delete_account(account_number)


        elif user_choice == "5":
            filename = input("Enter The File Name to Save Accounts: ") 
            manager.save_account(filename)


        elif user_choice == "6":
            filename = input("Enter The File Name to Load Accounts: ")
            manager.load_account(filename)


        elif user_choice == "7":
            print("Exit Bank Manager")
            break


        else:
            print("Something Worng, Please Try Again") 



if __name__ == "__main__":
    main()                   


                            


#This is for Lab 13
user1 = BankAccount("Khulood", 500)

user1.deposit()
user1.withdraw()
user1.get_balance()
user1.get_account_holder()
user1.get_account_number()