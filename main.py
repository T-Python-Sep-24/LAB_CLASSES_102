from Bank.bankAccount import BankAccount
from Bank.accountManager import AccountManager
    
def main():
    '''
    Main function that contains all operations
    '''
    #Create two different bank accounts
    account1 = BankAccount("Ghaliah Banounah", 5000)
    account2 = BankAccount("Ibrahim Alanzi", 60000)

    #Print info of the fisrt account before attempting withdraw
    print(account1.info())
    #Try to withdraw more than the account balance
    account1.withdraw(7000)
    #Print info of the first account after attempting withdraw
    print(account1.info())

    print()

    #Print info of the second account before attempting deposit
    print(account2.info())
    #Try to deposit 
    account2.deposit(5000)
    #Print info of the second account after attempting deposit
    print(account2.info())

def bonusMain():
    '''
    bonusMain() function that contains all operations for the bonus solution
    '''

    print("----Welcome to Bank Management program----")
    #Creating an instance of AccountManager class to be able to call its methods
    accountManager: AccountManager = AccountManager()
    while True:
        print("What do you want to do?")
        print("1. Add a Bank Account.\n2. Display All Accounts.\n3. Search for a Bank Account.\n4. Delete a Bank Account.\n5. Exit.")
        choice: str = input("Your choice: ")

        if choice == '1':
            #Creating new instance of BankAccount and storing it in the system using addAccount()
            accountHolder: str = input("Enter the name of the account holder: ")
            initialbalance: float = input("Enter the initial balance of the account: ")
            bankAcc: BankAccount = BankAccount(accountHolder, initialbalance)
            accountManager.addAccount(bankAcc)

        elif choice == '2':
            #Display all existing bank accounts in the system
            allAccounts: str = accountManager.displayAccounts()
            print(allAccounts)
            input("")

        elif choice == '3':
            #Make sure the user enters numbers only, keep prompting for the correct input
            while True:
                try:
                    accNumber: int = int(input("Please enter your account number: "))
                except ValueError:
                    print("Invalid entry, try again with numbers only.")
                else:
                    #Search for an bank account with a given account number from the user, if it exists print its info
                    accountInfo: str = accountManager.searchAccounts(accNumber)
                    print(accountInfo)
                    input("")
                    break
                    
        elif choice == '4':
            #Make sure the user enters numbers only, keep prompting for the correct input
            while True:
                try:
                    accNumber: int = int(input("Please enter your account number: "))
                except ValueError:
                    print("Invalid entry, try again with numbers only.")
                else:
                    #Delete an bank account with a given account number from the user, then print the returned message
                    msg :str = accountManager.deleteAccount(accNumber)
                    print(msg)
                    input("")
                    break

        elif choice == '5':
            print("Thank you for using the Bank Management program, come again soon.")
            break

        else: 
            print("Invalid choice, try again..")
            input("")

#Calling main() to execute the lab solution
# main()

#Calling bonusMain() to execute lab bonus solution
bonusMain()
