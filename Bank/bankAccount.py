#To generate bank account number
from random import randint

bankAccountNumbers: list = []

class BankAccount:
    
    def __init__(self, accountHolder: str, balance: int = 0):
        self.__accountHolder = accountHolder
        self.__balance = balance
        self.__accountNumber = self.setAccountNumber()
        
    def setAccountNumber(self) -> int:
        '''
        A method that auto generates a unique bank account number.
        '''
        #Generate a random 10 digit number
        accNumber: int = randint(1000000000, 9999999999)

        #Make sure the generated bank account number is unique, keep generating a new number if it's not
        while accNumber in bankAccountNumbers:
            accNumber = randint(1000000000, 9999999999)
        bankAccountNumbers.append(accNumber)

        return accNumber

    def getBalance(self) -> float:
        '''
        A method that returns the current account balance.
        '''
        return self.__balance

    def getAccountHolder(self) -> str:
        '''
        A method that returns the name of the account holder.
        '''
        return self.__accountHolder

    def getAccountNumber(self) -> int:
        '''
        A method that returns the account number of the account holder.
        '''
        return self.__accountNumber

    def deposit(self, amount: float) -> float:
        '''
        A method that accepts an amount and adds it to the account balance, then returns the updated balance.
        '''
        finalBalance = self.getBalance()
        finalBalance += amount
        self.__balance = finalBalance
        print(f"{amount} was successfully deposited to the current balance.")
        return finalBalance

    def withdraw(self, amount: float) -> float:
        '''
        A method hat accepts an amount and subtracts it from the account balance, then returns the updated balance only if there are sufficient funds in the account.
        If there are insufficient funds, it will print an error message and leave the balance unchanged.
        '''
        finalBalance = self.getBalance()
        finalBalance -= amount
        if finalBalance < 0:
            print(f"Insufficient funds. Current balance: {self.getBalance()}")
        else:
            self.__balance = finalBalance
        return finalBalance
    
    def info(self):
        '''
        A method that returns a string containing info of the account
        '''
        return f"Account number: {self.getAccountNumber()} Account Holder: {self.getAccountHolder()}. Current balance: {self.getBalance()}"
