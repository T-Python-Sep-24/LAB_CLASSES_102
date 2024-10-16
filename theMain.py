from Bank import *

menu = ''' 
1. add a bank account.
2. display bank accounts.
3. search for a bank account.
4. delete a bank account.
5. deposit
6. withdraw
7. exit.
'''

print('Account Manager System: \n')

manager = AccountManager()

while True:
    print(menu)
    choose = int(input('Choose the number of an action to do: '))
    print()
    if choose == 1:
        name = input('What is the account holder name?: ')
        deposit_choice = input('Do you want to deposit to your new account? (y or n): ')
        if deposit_choice.lower() == 'y':
            balance = float(input('How much do you want to deposit?: '))
        else:
            balance = 0
        newAccount = BankAccount(name, balance)
        manager.add_account(newAccount)

    elif choose == 2:
        try:
            manager.display_accounts()
        except Exception as e:
            print(e.__class__)

    elif choose == 3:
        account_to_search = input('Enter the account number you want to SEARCH: ')
        manager.search_accounts(account_to_search)

    elif choose == 4:
        account_to_delete = input('Enter the account number you want to DELETE: ')
        manager.delete_account(account_to_delete)

    elif choose == 5:
        account_deposit = input('Enter the account number you want to Deposit into: ')
        if manager.search_accounts(account_deposit):
            amount = float(input('How much do you want to deposit?: '))
            account = manager.accounts[account_deposit]
            account_instance = BankAccount(account['account_holder'], account['balance'])
            account_instance.deposit(amount)
            manager.save_to_file('accounts.pkl', manager.accounts)
            print('Your balance now:', account_instance.get_balance())

    elif choose == 6:
        account_withdraw = input('Enter the account number you want to Withdraw from: ')
        if manager.search_accounts(account_withdraw):
            amount = float(input('How much do you want to Withdraw?: '))
            account = manager.accounts[account_withdraw]
            account_instance = BankAccount(account['account_holder'], account['balance'])
            if account_instance.withdraw(amount):
                manager.save_to_file('accounts.pkl', manager.accounts)
                print('Your balance now:', account_instance.get_balance())

    elif choose == 7:
        print("Exiting Account Manager System. Thank you!")
        break
    else:
        print("wrng option. Please try again.")


