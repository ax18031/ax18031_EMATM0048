#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 12:54:31 2021

@author: jackmather
This file is to run the classes that I have implemented. 
"""
from Customer_Account_Class import customer_account
from Online_Bank_Class import online_bank

accounts_dict={} 
def main():
    def create_account():
        name = input('Enter your full name: ')
        age = int(input('Enter your age: '))
        address = input('Enter your address: ')
        balance = float(input('Enter your current balance: '))
        PIN = int(input('Enter your 4 digit PIN: '))
        customer= customer_account(name=name,age=age,address=address,balance=balance,PIN=PIN)
        accounts_dict[customer.account]=customer
        print('Account successfully created! Your account number is ', customer.account_number)
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
            create_account()
        elif int(num)==2:
            account_num= int(input('Enter your account number: '))
            PIN_num= int(input('Enter your PIN number: '))
            customer = customer_account
            accounts_dict[account_num]=customer
            customer.login(account_num,PIN_num)
            print('You have successfully logged in!')
        else:
            online_bank.logout()
            print('You have successfully logged out!')
            return
        print("""
              ====Online Banking App====
              Choose from the following
                       options:
              1. Withdraw Money
              2. Deposit Money
              3. Transfer Money
              4. Check Balance
              ==========================
              """)
        num1=input('Select an option by selecting a number: ')
        if int(num1)==1:
            accounts_dict[customer_account.account_number].withdraw()
        elif int(num1)==2:
            accounts_dict[customer_account.account_number].deposit()
        elif int(num1)==3:
            accounts_dict[customer_account.account_number].transfer()
        elif int(num1)==4:
            accounts_dict[customer_account.account_number].check_balance()
 
main()
    
    

        


