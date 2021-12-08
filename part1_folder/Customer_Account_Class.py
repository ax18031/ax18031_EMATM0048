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

import random
class Customer_Account:
    account_number = random.randint(1000000,9999999)
    
    def __init__(self,name,age,balance,pin):
        self.name = str(name)
        self.age = int(age)
        self.balance = float(balance)
        self.pin = int(pin)
        self.account = Customer_Account.account_number
        Customer_Account.account_number!=Customer_Account.account_number
        
    def showdetails(self):
        print('Name: '+ str(self.name) +
              'Age: '+ str(self.age) +
              'PIN: '+str(self.pin) +
              'Account Number: '+str(self.account))
    
    def createaccount(self):
        print('Account successfully created! Your Account Number is:',self.account)
                
    
class Customer_Action(Customer_Account):
    
    def __init__(self,name,age,pin,balance):
        super().__init__(name,age,balance,pin)

    def deposit(self,deposit_funds):
        self.deposit_funds = deposit_funds
        self.balance += self.deposit_funds
        self.total_deposits += 1
        print('Your new balance is £', self.balance)
    
    
    def withdraw(self,withdraw_funds):
        self.withdraw_funds = withdraw_funds
        if self.balance<self.withdraw_funds:
            return print('Insufficient funds to withdraw. Please try again!')
        else:
            self.balance -= self.withdraw_funds
            self.total_withdrawals += 1
            print('Withdrawal successful! Your balance is now £' , self.balance, '.')
    
    
    def transfer(self,transfer_funds,receiver):
        self.transfer_funds = transfer_funds
        self.receiver = receiver
        if self.transfer_funds < 1000 and self.balance>self.transfer_funds:
            self.balance -= self.transfer_funds
            self.total_transfers += 1
            print('Transfer successful! Your balance is now £', self.balance , '.')
        elif self.balance < self.transfer_funds:
            return print('Insufficient funds to withdraw. Please try again!')
        elif self.transfer_funds < 0:
            return print('Cannot transfer negative amounts!')
        elif self.transfer_funds>1000:
            return print('Transfer unsuccessful! Amount exceeds limit of £1000.')
            
    
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
    