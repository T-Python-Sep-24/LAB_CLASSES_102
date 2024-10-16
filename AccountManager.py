import os.path
import pickle
from BankAccount import BankAccount

class AccountManager():

    fileName = 'bank_accounts.pkl'
    def __init__(self):
        self.accounts = []

    def add_account(self, bankAccount: BankAccount):
        """
        This function allows the manager to add an account
        :param bankAccount:
        :return:
        """
        try:
            self.accounts.append(bankAccount)
            print(f" >>> ✅ Account {bankAccount.get_account_number()} ADDED SUCCESSFULLY , "
                  f"For Customer: {bankAccount.get_account_holder()} "
                  f"With balancce {bankAccount.get_balance()}")
            self.__save_to_file(self.fileName)
        except Exception as e:
            print(e)

    def display_accounts(self):
        """
        This Method displays all the account
        :return:
        """
        try:
            self.__load_from_file(self.fileName)
            print(" --------- Accounts ---------")
            for i, account in enumerate(self.accounts, start=1):
                print(f"{i}. Account {account.get_account_number()}, "
                      f"For Customer: {account.get_account_holder()} "
                      f"With balancce {account.get_account_holder()}")
            print(" --------- -------- ---------")
        except Exception as e:
            print(e)
    def search_accounts(self, account_number):
        """
        This method search for a particular account using its number
        :param account_number:
        :return:
        """

        try:
            accounts = self.__load_from_file(self.fileName)

            print(" --------- Accounts Founded ---------")
            for i, account in enumerate(accounts, start=1):
                if int(account.get_account_number()) == int(account_number):
                    print(f"{i}. Account number: {account.get_account_number()} "
                          f"for Customer {account.get_account_holder()} "
                          f"Have the balance {account.get_balance()}")
                else:
                    print("No match")
            print(" --------- -------- -------- ---------")

        except Exception as e:
            print(e)

    def delete_account(self, account_number):
        """
        This method deletes an account using its number
        :param account_number:
        :return:
        """

        accounts = self.__load_from_file(self.fileName)
        for i, account in enumerate(accounts, start=1):
            if int(account.get_account_number()) == int(account_number):
                self.accounts.remove(account)
                print("Account Deleted Successfully ✅")
                self.__save_to_file(self.fileName)
            else:
                print("No match")

        # for i in accounts:
        #     print(i.get_account_number())

    def __save_to_file(self, fileName):
        """
        This method save the accounts data to the pickle file after it has been serialized
        :param fileName:
        :return:
        """
        try:
            with open(fileName, 'wb') as f:
                pickle.dump(self.accounts, f)
        except Exception as e:
            print(e)

    def __load_from_file(self, fileName):
        """
        This method loads all the accounts data from the pickle file and deserialize it
        :param fileName:
        :return: accounts
        """
        
        try:
            with open(fileName, 'rb') as file:
                self.accounts = pickle.load(file)
                print(f"Loading Data ... ⏳")
                return self.accounts
        except Exception as e:
            print(f"Error loading from file The File is Empty: {e} ⚠ ")
