
from AccountManager import *
from BankAccount import *


while True:

      print("1. Add New Account \n2. Display All Accounts "
            "\n3. Search for Account \n4. Delete Account "
            "\nQ/q To quit")

      choice = (input("Enter Your Choice: "))

      if choice == "1":

            name = input("Enter account Holder Name: ")
            balance = int(input("Enter account Balance: "))
            account = BankAccount(name, balance)

            m = AccountManager(account)
            m.add_account(account)

            input(">>> Press Any key to continue <<<")

      elif choice == "2":
            m = AccountManager()
            m.display_accounts()
      elif choice == "3":
            pass
      elif choice == "4":
            pass
      elif choice.lower() == "q":
            print("Good Bay")
            break
      else:
            print("Enter a Valid Choice !!")


# c = BankAccount("hmzh", 1500)
# print(c.get_account_holder())
# print(c.get_balance())
# c.deposit(5000)
# c.withdraw(200)
# print(c.get_balance())
# d = BankAccount('ahmad')
# print(d.get_account_holder())
# print(d.get_account_number())