
from AccountManager import *
from BankAccount import *

def main():
      """
      This is the main function that interacts with the client and calls the other classes to complete required processes
      :return:
      """
      manager = AccountManager()
      while True:

            print("1. Add New Account "
                  "\n2. Display All Accounts "
                  "\n3. Search for Account "
                  "\n4. Delete Account "
                  "\nQ/q To quit")

            choice = (input("Enter Your Choice: "))

            if choice == "1":

                  name = input("Enter account holder name: ")
                  initial_balance = int(input("Enter initial balance: "))
                  account = BankAccount(name, initial_balance)
                  manager.add_account(account)

                  input(">>> Press Any key to continue <<<")

            elif choice == "2":
                  manager.display_accounts()
                  input(">>> Press Any key to continue <<<")
            elif choice == "3":
                  acc_num = input("Enter the account number to search for: ")
                  manager.search_accounts(acc_num)
                  input(">>> Press Any key to continue <<<")
            elif choice == "4":
                  acc_num = input("Enter the account number to delete: ")
                  manager.delete_account(acc_num)
                  input(">>> Press Any key to continue <<<")
            elif choice.lower() == "q":
                  print("Good Bye")
                  break
            else:
                  print("Enter a Valid Choice !!")
main()

# c = BankAccount("hmzh", 1500)
# print(c.get_account_holder())
# print(c.get_balance())
# c.deposit(5000)
# c.withdraw(200)
# print(c.get_balance())
# d = BankAccount('ahmad')
# print(d.get_account_holder())
# print(d.get_account_number())