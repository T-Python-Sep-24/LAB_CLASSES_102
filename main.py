
from AccountManager import *
from BankAccount import *

def main():
      """
      This is the main function that interacts with the client and calls the other classes to complete required processes.
      :return:
      """
      manager = AccountManager()
      while True:

            print()
            print(" ------- Welcome To H3D Bank ------- ")
            print(" 1. Add New Account "
                  "\n 2. Display All Accounts "
                  "\n 3. Search for Account "
                  "\n 4. Delete Account "
                  "\n Q/q To quit")
            print("-"*37)
            choice = (input(" Enter Your Choice: "))
            print()

            if choice == "1":

                  name = input("> Enter account holder name: ")
                  initilizeChoice = input("> Do You want to add balance (NOTE: 0 is the default balance amount) [Y/N] ? ")

                  if initilizeChoice.lower() == "y":

                        balance = float(input("> Enter initial balance: "))
                        account = BankAccount(name, balance)
                        manager.add_account(account)

                  elif initilizeChoice.lower() == "n":

                        account = BankAccount(name)
                        manager.add_account(account)
                  else:
                        print("Input Error,  please Try again later")
                  input(">>> Press Any key to continue <<<")

            elif choice == "2":

                  manager.display_accounts()
                  input(">>> Press Any key to continue <<<")

            elif choice == "3":

                  acc_num = int(input("> Enter the account number to search for: "))
                  manager.search_accounts(acc_num)
                  input(">>> Press Any key to continue <<<")

            elif choice == "4":

                  acc_num = int(input("> Enter the account number to delete: "))
                  manager.delete_account(acc_num)
                  input(">>> Press Any key to continue <<<")

            elif choice.lower() == "q":

                  print("Goodbye !")
                  break

            else:
                  print("> ⚠ Please enter a Valid Choice ⚠")

try:
      main()
except ValueError as e:
      print("> Please Try again and Enter a valid data ❌")
except Exception as e:
      print(e)


# c = BankAccount("hmzh", 1500)
# print(c.get_account_holder())
# print(c.get_balance())
# c.deposit(5000)
# c.withdraw(200)
# print(c.get_balance())
# d = BankAccount('ahmad')
# print(d.get_account_holder())
# print(d.get_account_number())