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
class customer_account():
    """this class contains information about the customer"""
    def __init__(self,name,age,address,balance,account_number,PIN):
        self.name = name
        self.age = age
        self.address = address
        self.balance = float(balance)
        self.account_number = int(account_number)
        self.PIN = int(PIN)
    def login(self):
        account_num= int(input('Enter your account number: '))
        PIN_num= int(input('Enter your PIN number: '))
        if self.account_number!= account_num  or self.PIN != PIN_num:
            print('Incorrect account number or PIN. Please try again.')
        else:
            print('Successfully logged in!')
    def deposit(self,deposit_funds):
        self.deposit_funds = deposit_funds
        self.balance += self.deposit_funds
        print('Your new balance is £', self.balance)
    def withdraw(self,withdraw_funds):
        self.withdraw_funds = withdraw_funds
        if self.balance< withdraw_funds:
            print('Insufficient funds to withdraw. Please try again!')
        else:
            self.balance -= self.withdraw_funds
            print('Withdrawal successful! Your balance is now £' , self.balance, '.')
    def transfer(self,sender,receiver, transfer_funds):
        if transfer_funds < 1000 and self.balance>transfer_funds:
            sender.withdraw(transfer_funds)
            receiver.deposit(transfer_funds)
            print('Transfer successful! Your balance is now £', self.balance , '.')
        elif self.balance < transfer_funds:
            print('Insufficient funds to withdraw. Please try again!')
        else:
            print('Transfer unsuccessful! Amount exceeds limit of £1000.')
    def check_balance(self):
        print('Your balance is: £',self.balance)
        
            
      
            

        
        
 
  
