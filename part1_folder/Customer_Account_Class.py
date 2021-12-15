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
from csv import DictReader
import random
import pandas as pd
import numpy as np

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
def getIndex(df,account):
    listofpositions = list()
    result = df.isin([account])
    seriesdf = result.any()
    column_names = list(seriesdf[seriesdf==True].index)
    for col in column_names:
        rows = list(result[col][result[col]==True].index)
        for row in rows:
            listofpositions.append(row,col)
    return listofpositions
    

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
        print('Name: '+ str(self.name) + 
              ' Age: '+ str(self.age) +
              ' PIN: '+str(self.pin) +
              ' Account Number: '+str(self.account)) # it is a simple print function 
    
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
        
    
    def deposit(self,deposit_funds):
        """This function allows users to depoit money into their bank account.
        The input is the amount the user wants to deposit into their account."""
        self.deposit_funds = deposit_funds 
        self.balance += self.deposit_funds #the balance of the user is now balance + deposit fund
        print('Your new balance is £', self.balance) # new balance is stated
    
    
    def withdraw(self,withdraw_funds):
        """This function allows users to withdraw money from their bank account.
        The input is the amount the user wants to withdraw from their bank account."""
        self.withdraw_funds = withdraw_funds
        if self.balance<self.withdraw_funds:#if their balance is lower than the 
            #input then they don't have enough money to withdraw
            return print('Insufficient funds to withdraw. Please try again!')
        else:
            self.balance -= self.withdraw_funds #the balance of the user is now 
            #balance - withdraw fund
            print('Withdrawal successful! Your balance is now £' , self.balance, '.')
            # new balance is stated
    
    
    def transfer(self,transfer_funds,receiver):
        """This function allows user to transfer money from their bank account
        into another users bank account up to £1000. The input is the amount 
        the user wants to transfer and the account number of the transferee."""
        self.transfer_funds = transfer_funds
        self.receiver = receiver
        if self.transfer_funds < 1000 and self.balance>self.transfer_funds: #restricted to £1000 
            #and their balance must be higher than the amount they want to transfer
            self.balance -= self.transfer_funds
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
        return print('Your PIN is: ',self.pin)
    
    def getBalance(self):
        return print('Your Balance is £', self.balance)
    
    def getAge(self):
        return print('Your age is: ', self.age)
    
    def getAccountNumber(self):
        return print('Your account number is: ',self.account_number)
    
    def getName(self):
        return print('The name under your account is ',self.name)
    
    def logout(self):

        

    
        
        

