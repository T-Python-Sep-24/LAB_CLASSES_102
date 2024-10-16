import pickle
class AccountManager:
    def __init__(self) -> None:
        self.Accounts=[]

    def add_account(self,BankAccount):
        self.Accounts.append(BankAccount)
    
    def display_accounts(self):
        if not self.Accounts:
            print("there is no account added yet!")
            return
        for account in self.Accounts:
            print(f"Account Number: {account.get_accountnumber()}\tAccount Holder: {account.get_accountholder()}"
                      f"\tAccount Balance: {account.get_balance()} ")
        
 
    def delete_account(self,account_number):
        if not self.Accounts:
            print("there is no account added yet!")
            return
        for account in self.Accounts:
            if account.get_accountnumber()==account_number:
                self.Accounts.remove(account)
                print("account has been deleted")
                return
        else:
            print("there is no account with this number")
            return
        
    def search_account(self,account_number:int):
        if not self.Accounts:
            print("there is no account added yet!")
            return
        for account in self.Accounts:
            if account.get_accountnumber()==account_number:
                print(f"Account Number: {account.get_accountnumber()}\tAccount Holder: {account.get_accountholder()}"
                      f"\tAccount Balance: {account.get_balance()} ")
                return
        else:
            print("there is no account with this number")
            return
    
    def save_to_file(self,file_name:str):
        with open (file_name,'wb')as file:
            pickle.dump(self.Accounts,file)
            

    def read_from_file(self,file_name:str):
        print("Trying to read an existing file...")
        try:
            with open (file_name,'rb')as file:
                self.Accounts=pickle.load(file)

        except FileNotFoundError:
            print("there is no file for the previous uses creating one ... ")
        except Exception as e:
            print("Error occurred",e.__class__,sep=': ')
            