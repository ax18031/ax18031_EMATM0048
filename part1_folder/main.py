#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 12:54:31 2021

@author: jackmather
This file is to run the classes that I have implemented. 
"""
from Customer_Account_Class import Customer_Action, Customer_Account, Savings_Account, Checking_Account
import pandas as pd
import numpy as np

def menu(user):
    """"This function acts as the way customers interact with the banking system
    once they have logged into their account or created an account with us."""
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
              6. Change your PIN
              7. Logout
              8. Previous Page
              ==========================
              """)
        num1 = int(input('Enter a number to select an option: ')) #user inputs a number to access a service
        if int(num1)==1 and user!= None:
            deposit_funds = float(input('How much money would you like to deposit?'))#deposit 
            user.deposit(deposit_funds)
        if int(num1)==2 and user!=None:
            withdraw_funds = float(input('How much money would you like to withdraw?'))#withdraw
            user.withdraw(withdraw_funds)
        if int(num1)==3 and user != None:
            transfer_funds = float(input('Enter the amount you would like to transfer: '))#transfer
            receiver = int(input('Enter the account number of the person you would like to transfer to.'))
            user.transfer(transfer_funds,receiver)
        if int(num1)==4 and user != None:
            user.getBalance()#retrieve balance
        if int(num1)==5 and user!=None:
            user.showdetails()#shows information about the user
            user.getBalance()
        if int(num1)==6 and user!= None:
            user.changePIN() #allows a user to change their pin
        if int(num1)==7 and user!= None:
            user.logout() #allows users to logout
            break
        if int(num1)==8:
            user.logout() #automatically updates when they go back to the previous menu
            break

def login(account_num,pin_num):
    df = pd.read_csv('customer_accounts.csv')
    df_k = df.loc[df['Account Number']==account_num]
    if np.array(df_k['PIN'])== pin_num and np.array(df_k['Account Number'])== account_num:
        print('Login Successful! Welcome to the online bank interface ')
        return True
    else:
        print('Login Failed! Please try again')
        return False

def main():
    while True:
        print("""
              ====Online Banking App====
                Welcome to the online
                  Banking Interface
              
              Would you like to:
                  1. Create an account
                  2. Login
                  3. Freeze Account
              ==========================
              """)
        num = int(input('Enter a number to select an option: '))
        if num == 1:
            account_type = int(input('Would you like to open a [1] Current, [2] Checking or [3] Savings Account?'))
            name = str(input('Please enter your name: '))
            age = int(input('Please enter your age: '))
            balance = float(input('Please enter your initial balance: '))
            pin = int(input('Please enter your 4 digit PIN: '))
            user = Customer_Account(name,age,balance,pin)
            if account_type == 1:
                user_customer_action = Customer_Action(user.name,user.age,user.balance,user.pin)
                user_customer_action.createaccount()
                menu(user_customer_action)
            elif account_type == 2:
                user_checking = Checking_Account(user.name,user.age,user.balance,user.pin)
                user_checking.createaccount()
                menu(user_checking)
            elif account_type == 3:
                user_savings = Savings_Account(user.name,user.age,user.balance,user.pin)
                user_savings.createaccount()
                menu(user_savings)
        elif num ==2:
            account_num = int(input('Please enter your Account Number: '))
            pin_num = int(input('Please enter your PIN:'))
            login_user = login(account_num,pin_num)
            if login_user == True:
                df = pd.read_csv('customer_accounts.csv')
                df_data = df.loc[df['Account Number']== account_num]
                name1 = df_data['Name']
                age1 = df_data['Age']
                balance1 = df_data['Balance']
                pin1 = df_data['PIN']
                user = Customer_Account(name1,age1,balance1,pin1)
                user1 = Customer_Action(user.name,user.age,user.balance,user.pin)
                menu(user1)
        elif num == 3:
            choice = str(input('Do you still wish to freeze your account? Type (Y/N)'))
            if choice == 'Y':
                name2 = str(input('Please enter the name on the account you wish to freeze: '))
                age2 = int(input('Please enter your age: '))
                balance2 = float(input('Please enter your current balance: '))
                account2 = int(input('Please enter your account number: '))
                pin2 = int(input('Please enter your 4 digit PIN: '))
                user2 = Customer_Account(name2,age2,balance2,pin2)
                user2.freeze_acc(account2,pin2)
            elif choice == 'N':
                print('Thank you! Your account has not been frozen.') 
                
 
main()               
 
                

    




        
        

        
        
       




        


