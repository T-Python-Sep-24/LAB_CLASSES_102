from Bank.Bank import BankAccount as acc
from Bank.Bankmanagement import AccountManager

manager = AccountManager()
manager.read_from_file("Accounts.pkl")
print("-"*10,"Bank management System","-"*15)
while True:
    print('1. Add account')
    print('2. show accounts')
    print('3. search for an account')
    print('4. delete account')
    print('5. Exit')
    choice=input("Enter your choice: ")
    if choice=='1':
        try:
            name=str(input("Enter Account holder's name: ")).strip()
            if any(char.isdigit()for char in name):
                raise ValueError("Name can not contain number")
            init_balance=float(input("enter initial balance: "))
            account=acc(name,init_balance)
            manager.add_account(account)
            print("Account added successfully!")
            input("\npress space to continue...")
        except ValueError as e:
            print(e)
            input("\npress space to continue...")
        except Exception as e:
            print("Error has occured: ",e.__class__)
    
    elif choice=='2':
        manager.display_accounts()
        input("\npress space to continue...")
    
    elif choice=='3':
        try:
            account_number=int(input("enter the account number you want to search for  :"))
            manager.search_account(account_number)
            input("\npress space to continue...")
        except ValueError:
            print('it only accept integer values!!!')
            input("\npress space to continue...")

    elif choice=='4':
        try:
            account_number=int(input("enter the account number you want to delete  :"))
            manager.delete_account(account_number)
            input("\npress space to continue...")
        except ValueError:
            print('it only accept integer values!!!')
            input("\npress space to continue...")
        
    
    elif choice=='5':
        manager.save_to_file("Accounts.pkl")
        break
    else:
        print("invalid choice!")
        input("\npress space to continue...")
        

