from Bank.bankAccount import BankAccount
import pickle

class AccountManager:

    bankAccounts : list[BankAccount] = []
    def __init__(self) -> None:
        pass

    def addAccount(self, bankAccount: BankAccount) -> str:
        '''
        This method adds a bank account to the collection.
        '''
        self.bankAccounts.append(bankAccount)
        self.__saveToFile("Bank/allBankAccounts.pkl")
        return f"Account Number: {bankAccount.getAccountNumber()} was successfully added to the system."

    def displayAccounts(self) -> str:
        '''
        This method displays all accounts in the collection.
        '''
        #Load the collection of bank accounts from the pickle file
        self.bankAccounts = self.__loadFromFile("Bank/allBankAccounts.pkl")

        formattedList: str = ""
        for i, acc in enumerate(self.bankAccounts):
            formattedList += f"{i + 1}. Account Holder: {acc.getAccountHolder()}, Account No.: {acc.getAccountNumber()}, Current Balance: {acc.getBalance()}\n"

        return formattedList
        
    def searchAccounts(self, accountNumber: int) -> str:
        '''
        This method searches for an account using the account number then returns information of that account if exists.
        '''
        #Load the collection of bank accounts from the pickle file
        self.bankAccounts = self.__loadFromFile("Bank/allBankAccounts.pkl")
        for acc in self.bankAccounts:
            if acc.getAccountNumber() == accountNumber:
                return acc.info()
        else:
            return "Account doesn't exist"    
        
    def deleteAccount(self, accountNumber: int) -> str:
        '''
        This method deletes an account from the bankAccounts collection using the account number.
        '''
        #Load the collection of bank accounts from the pickle file
        self.bankAccounts = self.__loadFromFile("Bank/allBankAccounts.pkl")

        for i, acc in enumerate(self.bankAccounts):
            if acc.getAccountNumber() == accountNumber:
                del self.bankAccounts[i]
                self.__saveToFile("Bank/allBankAccounts.pkl")
                return f"Account with number {accountNumber} was deleted successfully"
        else:
            return "The account doesn't exist."

    def __saveToFile(self, filename: str):
        '''
        This method saves the list of accounts to a pickle file.
        '''
        with open(filename, "wb") as file:
            #Store list of bank accounts in a pickle file
            pickle.dump(self.bankAccounts, file)

    def __loadFromFile(self, filename: str) -> list[BankAccount]:
        '''
        This method loads the list of acounts from a pickle file.
        '''
        try:
            with open(filename, "rb") as file:
                #Read the list of bank accounts from a pickle file and store it in bankAccounts list
                self.bankAccounts = pickle.load(file)
        except FileNotFoundError:
            print(f"File '{filename}' doesn't exist.")
        except Exception as e:
            print(e)
        else:
            return self.bankAccounts
