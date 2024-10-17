import random

# define a class for accounts data
class AccountsData:
    def __init__(self) -> None:
        self.__accounts_list = [] # private attribute (encapsultion)
    
    # getter to get accounts numbers list
    def get_accounts_list(self) -> list:
        return self.__accounts_list
    

    # setter to append the new account 
    def set_append_accounts_list(self, account):
        self.__accounts_list.append(account)


    # setter to extend new accounts list 
    def set_extend_accounts_list(self, account):
        self.__accounts_list.extend(account)


    # setter to remove account from the list
    def set_remove_accounts_list(self, account):
        self.__accounts_list.remove(account)
    


# define a class for bank accounts
class BankAccount:
    def __init__(self, account_holder: str, accounts_data: AccountsData, initial_balance: float = 0) -> None:
        self.__account_holder = account_holder
        self.__account_number = self.__set_account_number(accounts_data)
        self.__balance = initial_balance
        # store the account to account_data instance 
        accounts_data.set_append_accounts_list(self)


    # private method to set unique account number (abstraction)
    def __set_account_number(self, accounts_data):
        while True:
            account_number = random.randint(1000000000,9999999999)
            # get all the accounts to check if current account number is unique
            accounts_list = accounts_data.get_accounts_list()


            """ testing adding this block"""
            # print(f"**** Generated account number {account_number} successfully ****")
            return account_number
        
            """ testing remove this block"""
            if len(accounts_list) > 0:
                for i in accounts_list:
                    print(f"inside setAccountNumber -> acountsList type of i: {type(i)}")
                    print(f"inside setAccountNumber -> acountsList i: {i}")
                    print(f"i[0]: {type(i.get_accounts_list())}")
                    if account_number != i.get_account_number():
                        print(f"account number : {account_number}  result: {i.get_account_number()}")
                        print(f"**** Generated account number {account_number} successfully ****")
                        return account_number
            if len(accounts_list) == 0:
                return account_number
            """ end of testing"""

    def deposit(self, amount: float) -> float:
        self.__balance += amount
        print(f"**** {amount} successfuly deposited to your account, new balance: {self.__balance} ****")
        return self.__balance
    

    def withdraw(self, amount: float) -> float:
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"**** {amount} successfuly withdrew from your account, new balance: {self.__balance} ****")
            return self.__balance
        else:
            print(f" ---- Insufficient funds you can't withdraw {amount} ----")
        
    
    def get_balance(self) -> float:
        return self.__balance
    

    def get_account_holder(self) -> str:
        return self.__account_holder


    def get_account_number(self) -> int:
        return self.__account_number