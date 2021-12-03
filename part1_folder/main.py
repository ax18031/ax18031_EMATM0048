#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 12:54:31 2021

@author: jackmather
This file is to run the classes that I have implemented. 
"""
from Customer_Account_Class import customer_account
def main():

    while True:
        print("""
              ====Online Banking App====
              Welcome to your Online
              Banking User Interface
              Would you like to:
              1. Create an account
              2. Login
              ==========================
              """)
        num = input('Select an option by selecting a number: ')
        if int(num)==1:
            name = str(input('Enter your name: '))
            age = int(input('Enter your age: '))
            address = str(input('Enter your address: '))
            balance = float(input('Enter your balance: '))
            PIN = int(input('Enter your 4 digit PIN :'))
            customer = customer_account(name,age,address,balance,PIN)
            customer.create_account()
        
        elif int(num)==2:
            account= int(input('Please enter your account number: '))
            pin = int(input('Please enter your 4 digit PIN: '))
            customer.login(account,pin)
        break
     
    while True:  
        print("""
              ====Online Banking App====
              Choose from the following 
              options:
              1. Deposit money
              2. Withdraw money
              3. Transfer Funds
              4. Check Balance
              5. Check account details
              ==========================
              """)
        num1 = input('Select an option by selecting a number: ')
        if int(num1)==1:
            deposit_funds = float(input('How much money would you like to deposit?'))
            customer.deposit(deposit_funds)
        if int(num1)==2:
            withdraw_funds = float(input('How much money would you like to withdraw?'))
            customer.withdraw(withdraw_funds)
        if int(num1)==3:
            transfer_funds = float(input('Enter the amount you would like to transfer: '))
            receiver = customer_account(name=None,age,address,balance,PIN)
            customer.transfer(transfer_funds,receiver)
        if int(num1)==4:
            customer.check_balance()
        if int(num1)==5:
            customer.getName()
            customer.getAge()
            customer.getAddress()
            customer.getBalance
            customer.getAccountNumber()
            customer.getPIN()

    


main()        




        


