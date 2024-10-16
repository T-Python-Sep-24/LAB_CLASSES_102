# LAB_CLASSES_102


Create a Python class called `BankAccount` that simulates a simple bank account. The class should have the following functionalities:

1. It should have a constructor that accepts the `account_holder` name and initial balance (`initial_balance`), setting the balance to zero if the initial balance is not provided.
- another attribute `account_number` should be set automatically inside the initializer , auto generated bank account number. make sure it is 10 numbers and unique (not generated before for another account)

2. A method called `deposit` that accepts an amount and adds it to the account balance, and then returns the updated balance.
3. A method called `withdraw` that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should print an error message and leave the balance unchanged.
4. A method called `get_balance` that returns the current account balance.
5. A method called `get_account_holder` that returns the name of the account holder.
6. A method called `get_account_number` that returns the number of the account holder.

#### Note: OOP principle where applicable such as Encapsulation, Abstraction, etc. & Use modules (& packages if needed) to organize your code. 

---------

# Bonus 
## Using your previous class `BankAccount` , we want to create a Bank Manager program.
### Objective:
Create a Python program to manage a list of accounts using classes and persist to file storage using `pickle` module. The program will allow Bank managers to add new accounts, display the list of accounts, and save/load the accounts from a file, search for an account, delete an account, update an account.

### Steps:

#### Define the `BankAccount` Class (should be done from the first LAB)


#### Create a class named `AccountManager` to manage a collection of bank accounts.
The AccountManager class should have the following methods:
- add_account(self, bank_account: BankAccount): Adds a bank account to the collection.
- display_accounts(self): Displays all accounts in the collection.
- search_accounts(self, account_number): searches for an account using the account number.
- delete_account(self, account_number): delete the account from the AccountManager collection using the account number.
- save_to_file(self, filename: str): Saves the list of accounts to a pickle file.
- load_from_file(self, filename: str): Loads the list of acounts from a pickle file.


#### Implement Pickle File I/O:

- The save_to_file method should serialize the list of bank accounts to a pickle file.
- The load_from_file method should deserialize the pickle file and recreate the list of bank accounts.


#### Create the Main Program:

- Provide a menu for the user to choose actions: add a bank account, display bank accounts, search for a bank account, delete a bank account , or exit.
- Implement the logic to handle each menu option.
- Use good practices, such as handling exceptions using Try...Except
