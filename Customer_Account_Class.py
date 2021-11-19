#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:11:43 2021

@author: jackmather

This file contains the customer account class. This class contains information
about the customer such as name, address, etc... This class can:

Login to the bank system, account number and PIN
Transfer money from their account to another valid account
Deposit funds
Withdraw Funds
"""
class customer_account:
    """this class contains information about the customer"""
    def __init__(self,name,address,balance,account_number,PIN):
        self.name = name
        self.address = address
        self.balance = balance
        self.account_number = account_number
        self.PIN = PIN
    def login(self):
        value2 = int(input('Enter Account Number...' ))
        value3 = int(input('Enter PIN Number...' ))
        if value2 != self.account_number or value3 != self.PIN:
            print('Incorrect account number or PIN. Please try again.')
        else:
            print('Successfully logged in!')
    def deposit(self):
        deposit_funds=float(input('Amount you would like to deposit...'))
        self.balance += deposit_funds
        print('Your new balance is ' + str(self.balance))
    def withdraw(self):
        withdraw_funds = float(input('Amount you would like to withdraw' ))
        if self.balance<withdraw_funds:
            print('Insufficient funds to withdraw. Please try again!')
        else:
            self.balance -= withdraw_funds
            print('Withdrawal successful! Your balance is now ' + str(self.balance)+'.')
    def balance(self):
        return self.balance
        
        
 
  
