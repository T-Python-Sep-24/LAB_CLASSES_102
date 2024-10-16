import sys
import os
import pickle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BankClasses import BankAccount

class AccountManager(BankAccount):
    def __init__(self) -> None:
        self.__data=[]

    def __save_to_file(self, filename: str):
        try:
            with open(filename,'wb') as file:
                pickle.dump(self.__data,file)
        except Exception as e:
            print(f"Error saving data to file: {e}")        

    def __load_from_file(self, filename: str):
        try:
            with open(filename,'rb') as file:
                return pickle.load(file) 
        except Exception as e:
            print(f"Error loading data from file: {e}")    

    def add_account(self, bank_account:BankAccount):
        uniqe_account_number=bank_account.get_account_number()
        for i in self.__data:
           while uniqe_account_number==self.__data[i]['number']:
               uniqe_account_number=bank_account.get_account_number()
        account={
            "name":bank_account.get_account_holder(),
            "balance":bank_account.get_balance(),
            "number":uniqe_account_number
        }
        self.__data.append(account)
        self.__save_to_file('accounts.pkl')

    def display_accounts(self):
        accounts_list=self.__load_from_file('accounts.pkl')
        print()
        for index,item in enumerate(accounts_list,start=1):
            print(f"{index}. Name: {item['name']}.\nAccount Number: {item['number']}\nBalance: {item['balance']}\n")
        

    def search_accounts(self, account_number):
        accounts_list=self.__load_from_file('accounts.pkl')
        for index,item in enumerate(accounts_list,start=1):
            if account_number == item['number']:
                return f"{index}. Name: {item['name']}.\nAccount Number: {item['number']}\nBalance: {item['balance']}\n"

        else:
             return f"({account_number}) Not found."    
    
    def delete_account(self, account_number):
        accounts_list=self.__load_from_file('accounts.pkl')
        for item in accounts_list:
            if account_number == item['number']:
                accounts_list.remove(item)
                self.__data=accounts_list[:]
                self.__save_to_file('accounts.pkl')
                return "Account deleted successfully"

        else:
             return f"({account_number}) Not found." 
        
  
    