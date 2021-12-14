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

class Customer_Account:
    account_number = random.randint(1000000,9999999)
    
    def __init__(self,name,age,balance,pin):
        self.name = str(name)
        self.age = int(age)
        self.balance = float(balance)
        self.pin = int(pin)
        self.account = Customer_Account.account_number
        Customer_Account.account_number += 1
        Customer_Account.account_number!=Customer_Account.account_number
        
        
    def showdetails(self):
        print('Name: '+ str(self.name) +
              ' Age: '+ str(self.age) +
              ' PIN: '+str(self.pin) +
              ' Account Number: '+str(self.account))
    
    def createaccount(self):
         if self.name == "" or self.age == "" or self.balance == "" or self.pin == "":
             print('Must complete all fields! Please try again.')
             return
         data = [self.name,self.age,self.balance,self.account,self.pin]
         self.data = data
         with open('customer_accounts.csv','a',encoding='UTF8') as f:
             write = csv.writer(f)
             write.writerow(self.data)
             write.writerow([])
             f.close()
         print('Your account has been successfully created! Your account number is: ', self.account)
    

    

           
           

    
# Child Class
class Customer_Action(Customer_Account):
    
    def __init__(self,name,age,balance,pin):
        super().__init__(name,age,balance,pin)

    
    def deposit(self,deposit_funds):
        self.deposit_funds = deposit_funds
        self.balance += self.deposit_funds      
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
                with open('customer_accounts.csv','a') as f:
                    dict_reader = DictReader(f)
                    list_dict = list(dict_reader)
                    for dictionary in list_dict:
                        if dictionary['Account Number']==self.account:
                            dictionary['PIN']==self.pin
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
    
    def freeze_acc(self,acc,pins):
        with open('customer_accounts.csv','r') as f:
            dict_reader = DictReader(f)
            list_dict = list(dict_reader) 
            for dictionary in list_dict:
                if (dictionary['Account Number']==acc) and (dictionary['PIN']==pins):
                    Customer_Account.login == False
                    Customer_Action.transfer == False
                    print('Account Successfully Frozen!')
                    return True
                else:
                    print('Incorrect account number/PIN or account does not exist!' )
                    return False
    

