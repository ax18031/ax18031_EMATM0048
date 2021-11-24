#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 12:54:31 2021

@author: jackmather
This file is to run the classes that I have implemented. 
"""
from Customer_Account_Class import customer_account
from Online_Bank_Class import online_bank

def main():
    while True:
        customers=[]
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
            name = input('Enter your name: ')
            age = int(input('Enter your age: '))
            address = input('Enter your address: ')
            balance = float(input('Enter your current balance: '))
            account_number = int(input('Enter your 7 digit account number: '))
            PIN_number = int(input('Enter your PIN number: '))
            customer = customer_account(name,age,address,balance,account_number,PIN_number)
            customers.append(customer)
            print('Account Successfully created!')
        elif int(num)==2:
            customer_account.login()
        else:
            online_bank.logout()
    while True:
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
        if int(num1==1):
            withdraw_funds=float(input('How much money would you like to withdraw?'))
            customer_account.withdraw(withdraw_funds)
    
    
    

        

            
John = ('John',32,'1 London Road',209,2022,3333)
Robyn = ('Robyn',22,'129 Ashley Road',900,7862,0000)      
main()
