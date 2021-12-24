#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:11:43 2021

@author: jackmather

This file contains the customer account class. This class contains information
about the customer such as name, age, etc... This class can:

Login to the bank system, account number and PIN
Transfer funds from their account to another valid account (up to £1000)
Deposit funds
Withdraw Funds
"""
import csv
import random
import pandas as pd
import numpy as np
import datetime



def login(account_num,pin_num):
    """This function is a login function which logs our customers in whom have
    already created an account with the interface"""
    df = pd.read_csv('customer_accounts.csv') #load our dataframe
    df_k = df.loc[df['Account Number']==account_num] # create a new dataframe with our row of interest
    if np.array(df_k['PIN'])== pin_num and np.array(df_k['Account Number'])== account_num: 
        # above, we use a numpy array to check if the account number and pin match our records
        print('Login Successful! Welcome to the online bank interface ') #successful login 
        return True
    else:# if the pin number and account number do not match our records, then login has failed!
        print('Login Failed! Please try again')
        return False

    

class Customer_Account:
    """This class allows users to show their details, create and freeze 
    their accounts """
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
        
        
    def showdetails(self):
        """This function shows the details of the user once logged in."""
        print('Name:',self.name)
        print('Age:',self.age)
        print('Account Number:',self.account)
        print('PIN:',self.pin)# it is a simple print function 
    
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
    
    def freeze_acc(self,account2,pin2):
        df = pd.read_csv('customer_accounts.csv')
        df_k = df.loc[df['Account Number']==account2]
        if np.array(df_k['PIN'])== pin2 and np.array(df_k['Account Number'])== account2:
            login == False
            Customer_Action.transfer == False
            print('Account successfully frozen! You will no longer be able to receive transfers or login to your account.')
        else:
            print('Incorrect account number/PIN or account does not exist!')
            
    

           
           

    
# Child Class
class Customer_Action(Customer_Account):
    """This class performs actions to the users account such as withdrawals,
    deposits, transfers. It is the child class of Customer_Account, so inheritance
    is used in this class."""
    
    def __init__(self,name,age,balance,pin):
        """This function initialises the class"""
        super().__init__(name,age,balance,pin)
        self.transaction_history = []
    
    def deposit(self,deposit_funds):
        """This function allows users to depoit money into their bank account.
        The input is the amount the user wants to deposit into their account."""
        self.deposit_funds = deposit_funds 
        self.balance += self.deposit_funds#the balance of the user is now balance + deposit fund
        time = datetime.datetime.now()
        self.trans_history(deposit_funds,'deposit',time)
        print('Your new balance is £', self.balance) # new balance is stated
    
    
    def withdraw(self,withdraw_funds):
        """This function allows users to withdraw money from their bank account.
        The input is the amount the user wants to withdraw from their bank account."""
        self.withdraw_funds = withdraw_funds
        if self.balance<self.withdraw_funds:#if their balance is lower than the 
            #input then they don't have enough money to withdraw
            return print('Insufficient funds to withdraw. Please try again!')
        else:
            self.balance -= self.withdraw_funds#the balance of the user is now 
            #balance - withdraw fund
            time = datetime.datetime.now()
            self.trans_history(withdraw_funds,'withdraw',time)
            print('Withdrawal successful! Your balance is now £' , self.balance, '.')
            # new balance is stated
    
    
    def transfer(self,transfer_funds,receiver):
        """This function allows user to transfer money from their bank account
        into another users bank account up to £1000. The input is the amount 
        the user wants to transfer and the account number of the transferee."""
        if transfer_funds < 1000 and self.balance>transfer_funds: #restricted to £1000 
            #and their balance must be higher than the amount they want to transfer
            self.withdraw(transfer_funds)
            receiver.deposit(transfer_funds)
            time = datetime.datetime.now()
            self.trans_history(transfer_funds,'transfer',time)
            print('Transfer successful! Your balance is now £', self.balance , '.')
            return True
        elif self.balance < self.transfer_funds: #balance less than the amount they want to transfer
            print('Insufficient funds to withdraw. Please try again!')
            return False
        elif self.transfer_funds < 0: #no negative numbers
            print('Cannot transfer negative amounts!')
            return False
        elif self.transfer_funds>1000: #can't transfer over £1000
            print('Transfer unsuccessful! Amount exceeds limit of £1000.')
            return False
        else:
            return False
        
    
    def changePIN(self):
        """This function allows users to change their pin"""
        p = int(input('Enter your current PIN: ')) #current pin 
        if p == self.pin: #checks if it is correct
            t = int(input('Enter your new PIN: '))#new pin
            if t!=self.pin:#checks it doesn't equal their old pin 
                self.pin = t #assigns self.pin to t
                print('Successfully updated your PIN! Your new PIN number is', self.pin)#successfully changed
            else:
                print('You have entered the sane PIN as before, Please enter a new one!')
                #lets users know they have entered their old pin
        else:
            print('Incorrect PIN provided! Please try again!') #wrong pin 
    
        
    
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
        df = pd.read_csv('customer_accounts.csv')
        df.loc[df['Account Number']==self.account,'Balance']= self.balance
        df.loc[df['Account Number']==self.account,'PIN']= self.pin
        df.to_csv('customer_accounts.csv',index=False)
        print('Logout Successful! Goodbye')
    
    def trans_history(self, amount, trans_type, time):
        if trans_type == 'deposit':
            data = ['Deposited £',amount,' at', time ,' balance is:',self.balance]
            self.transaction_history.append(data)
        elif trans_type == 'withdraw':
            data = ['Withdrew £',amount,' at', time,' balance is:',self.balance]
            self.transaction_history.append(data)
        elif trans_type == 'transfer':
            data = ['Transfered £',amount,' at', time,' balance is:',self.balance]
            self.transaction_history.append(data)
            
            
    def show_history(self):
        print(self.transaction_history)
        
        
class Checking_Account(Customer_Action):
    
    def __init__(self,name,age,balance,pin):
        super().__init__(name,age,balance,pin)
        
    def deposit(self,deposit_funds):
        self.balance *= 1.1
        Customer_Action.deposit(self,deposit_funds)
        
class Savings_Account(Customer_Action):
    
    def __init__(self,name,age,balance,pin):
        super().__init__(name,age,balance,pin)
        self.fee = 0.1*self.balance
        
    def withdraw(self,withdraw_funds):
        w = withdraw_funds+self.fee
        Customer_Action.withdraw(self,w)
        
    def transfer(self,transfer_funds,receiver):
        n = transfer_funds + self.fee
        Customer_Action.transfer(self,n,receiver)


class Freeze_Account(Customer_Account):
    
    def __init__(self,name,age,balance,pin):
        self.name = name
        self.age = age
        self.balance = balance
        self.pin = pin
    
    def login(self,account_num,pin_num):
        login(account_num,pin_num) = False
        print('Cannot Login since account is frozen')
        return False
    
    def transfer(self,transfer_funds,receiver):
        Customer_Action.transfer(transfer_funds,receiver)= False 
        print('Cannot Transfer Money! Account is frozen')
        return False
        
        

        
        

    
        
        

