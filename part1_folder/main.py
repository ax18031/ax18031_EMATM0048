#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 12:54:31 2021

@author: jackmather
This file is to run the classes that I have implemented. 
"""
from Customer_Account_Class import Customer_Action, Customer_Account


def menu(user):
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
        num1 = int(input('Enter a number to select an option: '))
        if int(num1)==1 and user !=None:
            deposit_funds = float(input('How much money would you like to deposit?'))
            user.deposit(deposit_funds)
        if int(num1)==2 and user != None:
            withdraw_funds = float(input('How much money would you like to withdraw?'))
            user.withdraw(withdraw_funds)
        if int(num1)==3 and user != None:
            transfer_funds = float(input('Enter the amount you would like to transfer: '))
            receiver = int(input('Enter the account number of the person you would like to transfer to.'))
            user.transfer(transfer_funds,receiver)
        if int(num1)==4 and user != None:
            user.getBalance()
        if int(num1)==5 and user!=None:
            user.showdetails()
            user.getBalance()

def main():
    while True:
        print("""
              ====Online Banking App====
                Welcome to the online
                  Banking Interface
              
              Would you like to:
                  1. Create an account
                  2. Login
              ==========================
              """)
        num = int(input('Enter a number to select an option: '))
        if num == 1:
            name = str(input('Please enter your full name: '))
            age = int(input('Please enter your age: '))
            balance = float(input('Please enter your balance: '))
            pin = int(input('Please enter your PIN: '))
            user = Customer_Account(name,age,balance,pin)
            user.createaccount()
            user_customer_action = Customer_Action(user.name,user.age,user.balance,user.pin)
            start = menu(user_customer_action)
            if start == False:
                break
main()
        
        

        
        
       




        


