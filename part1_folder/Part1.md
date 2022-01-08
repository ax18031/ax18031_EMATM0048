# SDPA Banking Project

This project arose the task of creating an online banking system that allowed users to create accounts, manage their money, change their PIN, and many other things.
In this file, I am going to give you a detailed report of my classes, functions, and methods to create a fully functioning banking system using Python and Object
Oriented Programming. I am going to be going through the two Python files and CSV file giving a full description of how I conquered the task presented to me.

Firstly, I am going to talk about all the classes I used to complete this task. The classes that I used to complete this task were all written in the file entitled
Customer_Account_Class.py. There were a total of 6 classes used in this project: Customer_Account, Customer_Action, Checking_Account, Savings_Account, 
Freeze_Account and Login_User. Customer_Account is the main parent class as it is the parent class of Customer_Action. All remaining classes are child classes of 
Customer_Action. These classes all worked together to create a fully functioning main programme implemented in the main.py file. This part of the project is where 
users can interact with classes using the text based interface that I created to work with the Object Oriented Programming.

I would like to talk about each the classes, their functions and attributes in chronological order. Customer_Account was the first class that I created when I 
started the project. This class contains an '__init__' fucntion which initialises name, age, balance, pin, and account number. I imported the Python library random 
for the account number to be unique. I specified that the account number had to be a random integer between 1,000,000 and 9,999,999 and that no account number can 
equal another persons account number. I made this so that the account number can act as a unique way for a customer to be identified when I needed a customer in the 
system (such as logging in/out). Further, I ensured that each input in the system was correct; e.g, age must be an integer, balance can be a float, and name must be 
a string. This makes the application stronger since you cannot enter strings for age and integers for name. The second and final function in this class was the 
createaccount function. The function allowed users to input their information into the system and write their data to the CSV file called 'customer_accounts.csv.' 
Using the Python library csv, I was able to write Python code that allowed my programme to write their information to the CSV file for their user information to be 
stored. 
Once this file closed, the system prints a success message and gives the users their account numbers.
The second class I created was called Customer_Action, which performed various tasks I needed my banking app to create. This class was the child class of Customer_
Account class which I just mentioned. The '__init__' function is the same apart from having an empty list called self.transactionhistory; this list fills up as many 
transactions take place where users can see their transaction history whilst using the interface. The first function showdetails shows the details of the customers. 
The second function called deposit allows customers to deposit money into their account, simple mathematics is used here to add the input amount to the current 
balance.
Withdraw function uses the same logic of withdrawing the inputted amount from the current balance, however, it was important to include logic to not allow the 
amount of money withdrawn to be greater than the current balance. Transfer used this same mathematics also having logic for if the amount the user wanted to 
transfer was less than their balance, I also included a rule which restricted the amount of money to be transferred to be less than 1000. changePIN function simply 
changes the users PIN, also has logic to not let the user change their pin to the same pin and if they enter the incorrect pin they cannot change their pin at all.
I had a list of 'get' functions, they get the users information allowing users to see their balance, age, account number, pin and name. 
Logout was the hardest function to write and it was the one that I had the most problems with. However, I resolved all the issues with this function. Logout simply 
updates the users information on the CSV file. It needed two ways of doing it as when a user simply creates their account their information is not on the CSV file 
so couldn't use the method implemented when a user logs in rather than creating an account. A mixture of pandas and csv was used here to implement the logout 
function. 
The last two functions in this class are the transaction history functions. The first of the transaction history function simply gets called when either deposit, 
transfer or withdrawn are called and writes down the amount of money deposited, withdrawn or transferred, the remaining balance and the time the transaction 
occurred. show_history function allows users to see their transaction histroy on the user interface in the main.py file. 

Moving onto the next two classes we have Checking_Account and Savings_Account. These two classes create two different types of accounts that one can have in my 
system. Using the super() function, I can get my __init__ function from the Parent Class Customer_Action. A checking account multiplies the current balance by 1.1 
each time a deposit is made whereas the savings account has a transaction fee of 10% of the balance each time a transfer or withdrawal is made. 

The Freeze_Account class is a child class of Customer_Action that doesn't allow a user to login or transfer money if they choose to freeze their account.

Finally, Login_User is a class that I created for users to login to their accounts. The function login uses pandas to read the dataframe to check that the correct 
information has been given to the system so it can verify a login. Users login to the system using their unique Account Number and their chosen PIN. The system then 
is initiated for them to use functions in the Customer_Action class. 

main.py file is where you can implement the text based user interface. The first menu asks users to login or create an account by inputting a numerical value. 
Depending on what they enter it asks them various questions. When creating an account, the system asks for the type of account (Current, Checking, or saving) and
then asks for name, age, initial balance, and PIN, then generates a unique and random account number for that user. It then triggers the main menu which contains 
actions that users can perform. If you choose to login, enter a valid account number and the pin related to that account, then you loginto the main menu.
The main menu has 9 options: Deposit, Withdraw, Transfer, Check Balance, Check account details, Change PIN, Transaction History, Freeze Account and Logout. The user 
can interact with this part of the system executing the defined functions in the classes written in the Customer_Account_Class.py file. 

The CSV file contains all the customers information with the columns representing the Name, Age, Balance, Account Number and PIN. 
