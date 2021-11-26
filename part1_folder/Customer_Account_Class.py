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

class customer_account():
    """this class contains information about the customer"""
    account_number = random.randint(1000000,9999999)
    def __init__(self,name,age,address,balance,PIN):
        self.name = name
        self.age = age
        self.address = address
        self.balance = float(balance)
        self.PIN = int(PIN)
        self.account = customer_account.account_number
        customer_account.account_number!=customer_account.account_number
    def login(self,account_num,PIN_num):
        account_num= int(input('Enter your account number: '))
        PIN_num= int(input('Enter your PIN number: '))
        if self.account!= account_num  or self.PIN != PIN_num:
            print('Incorrect account number or PIN. Please try again.')
        else:
            print('Successfully logged in!')
    def deposit(self):
        deposit_funds = float(input('How much money would you like to deposit?'))
        self.balance += deposit_funds
        print('Your new balance is £', self.balance)
    def withdraw(self):
        withdraw_funds=float(input('How much money would you like to withdraw?'))
        if self.balance<withdraw_funds:
            print('Insufficient funds to withdraw. Please try again!')
        else:
            self.balance -= withdraw_funds
            print('Withdrawal successful! Your balance is now £' , self.balance, '.')
    def transfer(self,receiver):
        transfer_funds = float(input('Enter the amount you would like to transfer: '))
        if transfer_funds < 1000 and self.balance>transfer_funds:
            self.balance -= transfer_funds
            receiver.balance += transfer_funds
            print('Transfer successful! Your balance is now £', self.balance , '.')
        elif self.balance < transfer_funds:
            print('Insufficient funds to withdraw. Please try again!')
        elif transfer_funds < 0:
            print('Cannot transfer negative amounts!')
        elif transfer_funds>1000:
            print('Transfer unsuccessful! Amount exceeds limit of £1000.')
    def check_balance(self):
        print('Your balance is: £',self.balance)
        
            
            

        
        
 
  
