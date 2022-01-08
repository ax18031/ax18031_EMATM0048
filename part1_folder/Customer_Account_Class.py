#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:11:43 2021

@author: jackmather
Name: Jack Mather
File Description: This file contains all the classes that I use in the main.py
file for an online banking system created using Object Oriented Programming.
The classes are Customer Account, Customer Action, Checking Account, Savings 
Account, Freeze Account and Login User. The Parent Class of Customer Action is 
Customer Account. Furthermore, Customer Action acts as the parent class of all 
the remaining classes in the repository. More details about the individual 
classes can be found on my GitHub repository in the Part1.md file.
"""
import csv
import random
import pandas as pd
import numpy as np
import datetime


class Customer_Account:
    """This class allows users to create account and generates an account number """
    account_number = random.randint(1000000,9999999)
    def __init__(self,name,age,balance,pin):
        """initialiser function for the variables"""
        self.name = str(name)
        self.age = int(age)
        self.balance = float(balance)
        self.pin = int(pin)
        self.account = Customer_Account.account_number #creates a random integer
        Customer_Account.account_number += 1
        Customer_Account.account_number!=Customer_Account.account_number
        # above customer account number cannot equal another persons 
    
    def createaccount(self):
        """This function creates a users account and adds their information to
        the csv file"""
        if self.name == "" or self.age == "" or self.balance == "" or self.pin == "": #empty values returns an error
             print('Must complete all fields! Please try again.')
             return
        data = [self.name,self.age,self.balance,self.account,self.pin] #contains all the account credentials of the user
        self.data = data
        with open('customer_accounts.csv','a',encoding='UTF8') as f: #opened the file and can append new information
             write = csv.writer(f)
             write.writerow(self.data) #writes the new row in the csv 
             write.writerow([])
             f.close()#closes the file when we have finished making ammendments
        print('Your account has been successfully created! Your account number is: ', self.account)
    

# Child Class
class Customer_Action(Customer_Account):
    """This class performs actions to the users account such as withdrawals,
    deposits, transfers. It is the child class of Customer_Account, so inheritance
    is used in this class."""
    
    def __init__(self,name,age,balance,account,pin):
        """This function initialises the class"""
        self.name = name
        self.age = age
        self.balance = balance
        self.account = account
        self.pin = pin
        self.transaction_history = []
    
    def showdetails(self):
        """This function shows the details of the user once logged in."""
        n = len(self.name)
        print('Name:',self.name[2:n-2])
        
        print('Age:',self.age)
        
        print('Account Number:',self.account)
        
        print('PIN:',self.pin)
        # it is a simple print function 
    
    def deposit(self,deposit_funds):
        """This function allows users to depoit money into their bank account.
        The input is the amount the user wants to deposit into their account."""
        if deposit_funds >= 0: 
            self.deposit_funds = deposit_funds 
            self.balance += self.deposit_funds#the balance of the user is now balance + deposit fund
            time = str(datetime.datetime.now())
            self.trans_history(deposit_funds,'deposit',time)
            print('Your new balance is £', self.balance)# new balance is stated
        else:
            print('Cannot deposit negative amount.')
    
    
    def withdraw(self,withdraw_funds):
        """This function allows users to withdraw money from their bank account.
        The input is the amount the user wants to withdraw from their bank account."""
        self.withdraw_funds = withdraw_funds
        if withdraw_funds >=0:
            if self.balance<self.withdraw_funds:#if their balance is lower than the 
                #input then they don't have enough money to withdraw
                return print('Insufficient funds to withdraw. Please try again!')
            else:
                self.balance -= self.withdraw_funds#the balance of the user is now 
                #balance - withdraw fund
                time = str(datetime.datetime.now())
                self.trans_history(withdraw_funds,'withdraw',time)
                print('Withdrawal successful! Your balance is now £' , self.balance, '.')
            # new balance is stated
        else:
            print('Cannot withdraw negative amount.')
    
    
    def transfer(self,transfer_funds, account):
        """This function allows user to transfer money from their bank account
        into another users bank account up to £1000. The input is the amount 
        the user wants to transfer and the account number of the transferee."""
        df = pd.read_csv('customer_accounts.csv') #load our dataframe
        df_k = df.loc[df['Account Number']==account] # create a new dataframe with our row of interest
        if np.array(df_k['Account Number'])== account:
            name = df_k['Name']
            age = df_k['Age']
            balance = df_k['Balance']
            account = account 
            pin = df_k['PIN']
            user_account = Customer_Action(name,age,balance,account,pin)
            if transfer_funds>=0:
                if transfer_funds < 1000:#restricted to between 0 and 1000
                    if  self.balance > transfer_funds:#and their balance must be higher than the amount they want to transfer
                        self.balance -= transfer_funds
                        user_account.balance += transfer_funds
                        time = str(datetime.datetime.now())
                        self.trans_history(transfer_funds,'transfer',time)
                        df.loc[df['Account Number']== account,'Balance']= user_account.balance
                        df.to_csv('customer_accounts.csv',index=False)
                        print('Transfer successful! Your balance is now £', self.balance , '.')
                        return True
                    else: #balance less than the amount they want to transfer
                        print('Insufficient funds to transfer. Please try again!')
                        return False
                else: #can't transfer over £1000
                    print('Transfer unsuccessful! Amount exceeds limit of £1000.')
                    return False
            else:
                print('Cannot transfer negative amounts!')
                return False
        
    
    def changePIN(self):
        """This function allows users to change their pin"""
        p = int(input('Enter your current PIN: ')) #current pin 
        if p == self.pin: #checks if it is correct
            t = int(input('Enter your new PIN: '))#new pin
            if t!=self.pin:
                self.pin = t # updates self.pin to t
                print('Successfully changed PIN! Your new pin is ',self.pin) #success message, self.pin updated
            elif t==self.pin:
                print('You have entered your old PIN! Please try again!') #stops users from using their old pin as new
                return
        else:
            print('Incorrect PIN! Please try again') #wrong pin given at beginning 
    
        
    
    def getPIN(self):
        """This function allows users to retrieve their PIN after logging in."""
        return print('Your PIN is: ',self.pin)
    
    def getBalance(self):
        """This function allows users to retrieve their Balance after logging in."""
        return print('Your Balance is £', self.balance)
    
    def getAge(self):
        """This function allows users to retrieve their Age after logging in."""
        return print('Your age is: ', self.age)
    
    def getAccountNumber(self):
        """This function allows users to retrieve their Account Number after logging in."""
        return print('Your account number is: ',self.account)
    
    def getName(self):
        """This function allows users to retrieve their Name after logging in."""
        return print('The name under your account is ',self.name)
    
    def logout(self):
        """ This function allows users to logout and updates their information 
        in the csv file which we keep all the information stored into our system"""
        df=pd.read_csv('customer_accounts.csv')
        customer_list = [] #empty list
        n = len(self.name) 
        name = self.name[2:n-2] # since name is np.array gets rid of [''] and leaves name
        age = self.age
        balance = self.balance
        account = self.account
        pin = self.pin
        data = [name,age,balance,account,pin] #uses data defined above
        with open('customer_accounts.csv', 'r') as f: 
            reader = csv.reader(f) #reads csv
            customer_list.extend(reader) #adds information to the list
        i = df.index
        j = df['Account Number'] == self.account #condition
        q = i[j] #set a condition to find the index of
        l = q.tolist() # adds the index to list 
        s = l[0] #list is of length 1, so want the first entry of the list 
        if data in customer_list: #if data already exists, means not a new customer so the customer logged in
            row_change = {s+1: data} #index of the row we want to overwrite with the information 
            with open('customer_accounts.csv', 'w') as f:
                writer = csv.writer(f) #how we are going to write the csv
                for line, row in enumerate(customer_list): #for loop to find the line,row
                           d = row_change.get(line, row) #define the new row
                           writer.writerow(d) #write the new row
            print('Logout Successful! Goodbye')
        else: #customers who have just created account will use this section of the function 
            df = pd.read_csv('customer_accounts.csv')
            df.loc[df['Account Number']==self.account,'Balance']= self.balance #updated balance
            df.loc[df['Account Number']==self.account,'PIN']= self.pin #updated pin 
            df.to_csv('customer_accounts.csv',index=False) #write to the csv file without an index
            print('Logout Successful! Goodbye')
    
    def trans_history(self, amount, trans_type, time):
        """This function logs the transactions that occur in a session for a type
        of customer."""
        if trans_type == 'deposit': #records deposits
            data = ['Deposited £'+str(amount)+' at '+ time +'. Balance is: £'+str(self.balance)]
            self.transaction_history.append(data)
        elif trans_type == 'withdraw': #records withdrawals
            data = ['Withdrawn £'+str(amount)+' at '+time+'. Balance is: £'+str(self.balance)]
            self.transaction_history.append(data)
        elif trans_type == 'transfer': #records transfers
            data = ['Transfered £'+ str(amount)+' at '+time+'. Balance is: £'+str(self.balance)]
            self.transaction_history.append(data)
            
            
    def show_history(self):
        """Shows the transaction history of a user"""
        print(self.transaction_history)
        
        
class Checking_Account(Customer_Action):
    """Class contains functions related to checking accounts. This means that
    when a user deposits money there balance increases by 10%."""
    
    def __init__(self,name,age,balance,account,pin):
        """Initialises the function from Customer Action class"""
        super().__init__(name,age,balance,account,pin)
        
    def deposit(self,deposit_funds):
        """When the user deposits it uses this function instead of the other 
        deposit function"""
        self.balance *= 1.1 #when they deposit money they get interest of 10% of their original balance
        Customer_Action.deposit(self,deposit_funds)
        
class Savings_Account(Customer_Action):
    """Class contains functions related to savings accounts. This means that 
    when a user withdraws or transfers money there is a fee associated with that
    action."""
    
    def __init__(self,name,age,balance,account,pin):
        super().__init__(name,age,balance,account,pin)
        self.fee = 0.1*self.balance # we set the fee at 10% of the balance
        
    def withdraw(self,withdraw_funds):
        w = withdraw_funds+self.fee #we add the fee onto the withdrawal
        Customer_Action.withdraw(self,w) #we perform the Customer_Action withdraw function
        
    def transfer(self,transfer_funds,receiver):
        n = transfer_funds + self.fee #we add the fee onto the transfer fee
        Customer_Action.transfer(self,n,receiver) #we perform the Customer_Action transfer function


class Freeze_Account(Customer_Action):
    """This class contains functions related to a customer who has frozen their
    account. This means that this customer cannot login or receive transfers."""
    
    def __init__(self,name,age,balance,account,pin):
        self.name = name
        self.age = age
        self.balance = balance
        self.account = account
        self.pin = pin
    
    def login(self,account_num,pin_num):
        Login_User.login == False # this function no longer can work for a customer of this type.
        print('Cannot Login since account is frozen')
        return False
    
    def transfer(self,transfer_funds,receiver):
        Customer_Action.transfer(transfer_funds,receiver)== False #this function can no longer work for a customer of this type.
        print('Cannot Transfer Money! Account is frozen')
        return False


class Login_User(Customer_Action):
    """This class helps users login to the banking system."""
    def __init__(self,account,pin):
        self.account=account
        self.pin=pin
    
    def login(self,account_num,pin_num):
        """This function is a login function which logs our customers in whom have
        already created an account with the interface"""
        df = pd.read_csv('customer_accounts.csv') #load our dataframe
        df_k = df.loc[df['Account Number']==account_num] # create a new dataframe with our row of interest
        if np.array(df_k['PIN'])== pin_num and np.array(df_k['Account Number'])== account_num:
            self.account = account_num
            self.pin = pin_num
            self.name = np.array((df_k['Name']))
            self.age = np.array(df_k['Age'])
            self.balance = np.array(df_k['Balance'])
        # above, we use a numpy array to check if the account number and pin match our records
            print('Login Successful! Welcome to the online bank interface ') #successful login 
            return True
        else:# if the pin number and account number do not match our records, then login has failed!
            print('Login Failed! Please try again')
            return False

        
        
        

        
        

    
        
        

