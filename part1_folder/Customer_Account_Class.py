#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:11:43 2021

@author: jackmather

This file contains the customer account class. This class contains information
about the customer such as name, address, etc... This class can:

Login to the bank system, account number and PIN
Transfer funds from their account to another valid account (up to £1000)
Deposit funds
Withdraw Funds
"""
from DataStorage import Data_Storage
import csv
import pandas as pd

class Customer_Account:
    account_number = 0
    
    def __init__(self,name,age,balance,pin):
        self.name = str(name)
        self.age = int(age)
        self.balance = float(balance)
        self.pin = int(pin)
        self.account = Customer_Account.account_number
        Customer_Account.account_number += 1
        Customer_Account.account_number!=Customer_Account.account_number
        self.customer = Data_Storage()
        self.accounts_file = "customer_accounts.csv"
        
        
    def showdetails(self):
        print('Name: '+ str(self.name) +
              ' Age: '+ str(self.age) +
              ' PIN: '+str(self.pin) +
              ' Account Number: '+str(self.account))
    
    def createaccount(self):
        self.users_account = Customer_Account(self.name,self.age,self.balance,self.pin)
        customer_information = dict()
        customer_information['Name']=self.users_account.name
        customer_information['Age']=self.users_account.age
        customer_information['Balance']=self.users_account.balance
        customer_information['Account Number']=self.account
        customer_information['PIN']=self.users_account.pin
        self.Data_Storage.write(customer_information)
        print('Account successfully created! Your Account Number is:',self.account)

        
    
class Customer_Action(Customer_Account):
    
    def __init__(self,name,age,balance,pin):
        super().__init__(name,age,balance,pin)
        self.accounts_file = "customer_accounts.csv"
    
    def update(self,variable,index):
        with open(self.accounts_file) as customer_accounts:
            customer_reader = csv.reader(customer_accounts,delimiter=',')
            l = list(customer_reader)
            df = pd.DataFrame(l)
            df.columns=df.iloc[0]
            df=df.reindex(df.index.drop(0).reset_index(drop=True))
            df.to_csv(self.accounts_file,index=False)
    
    def update_balance(self,balance):
        self.update(balance,index=2)
    
    def update_pin(self,new_pin):
        self.update(new_pin,index=4)

    def deposit(self,deposit_funds):
        self.deposit_funds = deposit_funds
        balance = self.balance + self.deposit_funds
        self.update_balance(balance)
        print('Your new balance is £', self.balance)
    
    
    def withdraw(self,withdraw_funds):
        self.withdraw_funds = withdraw_funds
        if self.balance<self.withdraw_funds:
            return print('Insufficient funds to withdraw. Please try again!')
        else:
            self.balance -= self.withdraw_funds
            print('Withdrawal successful! Your balance is now £' , self.balance, '.')
    
    
    def transfer(self,transfer_funds,receiver):
        self.transfer_funds = transfer_funds
        self.receiver = receiver
        if self.transfer_funds < 1000 and self.balance>self.transfer_funds:
            self.balance -= self.transfer_funds
            print('Transfer successful! Your balance is now £', self.balance , '.')
        elif self.balance < self.transfer_funds:
            return print('Insufficient funds to withdraw. Please try again!')
        elif self.transfer_funds < 0:
            return print('Cannot transfer negative amounts!')
        elif self.transfer_funds>1000:
            return print('Transfer unsuccessful! Amount exceeds limit of £1000.')
            
    def changePIN(self):
        p = int(input('Enter your current PIN: '))
        if p == self.pin:
            t = int(input('Enter your new PIN: '))
            if t!=self.pin:
                self.pin = t
                self.update_pin(t)
                print('Successfully updated your PIN! Your new PIN number is', self.pin)
            else:
                print('You have entered the sane PIN as before, Please enter a new one!')
        else:
            print('Incorrect PIN provided! Please try again!')
    
        
    
    def getPIN(self):
        return print('Your PIN is: ',self.pin)
    
    def getBalance(self):
        return print('Your Balance is £: ', self.balance)
    
    def getAge(self):
        return print('Your age is: ', self.age)
    
    def getAccountNumber(self):
        return print('Your account number is: ',self.account_number)
    
    def getName(self):
        return print('The name under your account is ',self.name)
