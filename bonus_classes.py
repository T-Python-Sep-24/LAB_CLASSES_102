import pickle
from classes import BankAccount, AccountsData

# define AccountManager class
class AccountManager():
    def __init__(self, accounts_data: AccountsData) -> None:
        # load pickle file on initilization
        self.__load_from_file("data.pkl", accounts_data)


    # private method to save to pickle file (abstraction)
    def __save_to_file(self, filename: str, accounts_list: list):
        try:
            with open(filename, "wb") as file:
                pickle.dump(accounts_list, file)
        except Exception as e:
            print(f"---- Exception: {e} ----")
            input("")


    # private method to load pickle file (abstraction)
    def __load_from_file(self, filename: str, accounts_data: AccountsData):
        try: 
            with open(filename, "rb") as file:
                data = pickle.load(file)
                accounts_data.set_extend_accounts_list(data)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"---- Exception: {type(e)} ----")
            # input("")
            

    def add_account(self, bank_account: BankAccount, accounts_data):
        self.__save_to_file("data.pkl", accounts_data.get_accounts_list())
        print(f"**** Add account was completed sucessfully ****")
        input("")


    def display_accounts(self, accounts_data: AccountsData):
        if len(accounts_data.get_accounts_list()) < 1:
            print("---- there are no accounts ----")
            input("")
        else:
            account_list = accounts_data.get_accounts_list()
            for i in account_list:
                holder = i.get_account_holder()
                number = i.get_account_number()
                balance = i.get_balance()
                print(f"Account number: {number}  -  Account holder: {holder}  -  balance: {balance}")
            print(f"**** Display accounts was completed sucessfully ****")
            input("")

    
    def search_accounts(self, account_number: int, accounts_data: AccountsData):
        # get the list of available accounts
        account_list = accounts_data.get_accounts_list()

        for i in account_list:
            if account_number == str(i.get_account_number()):
                holder = i.get_account_holder()
                number = i.get_account_number()
                balance = i.get_balance()
                print(f"\nFound: Account number: {number}  -  Account holder: {holder}  -  balance: {balance}")
                print(f"**** Search account was completed sucessfully ****")
                input("")
                break
        else:
            print("---- The account doesn't exist ----")
            input("")

        
    def delete_account(self, account_number: int, accounts_data: AccountsData):
        # get the list of available accounts
        account_list = accounts_data.get_accounts_list()

        for i in account_list:
            if account_number == str(i.get_account_number()):
                accounts_data.set_remove_accounts_list(i)
                self.__save_to_file("data.pkl", account_list )
                print(f"\n**** Account removed sucessfully ****")
                input("")
                break
        else:
            print("---- The account doesn't exist ----")
            input("")