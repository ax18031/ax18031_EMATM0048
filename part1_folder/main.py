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
        customers=[]
        print("""
              ===Online Banking App===
              Welcome to your Online
              Banking User Interface
              
              Would you like to:
              1. Create an account
              2. Login
              ========================
              """)
        num = input('Enter a number: ')
        if int(num)==1:
            name = input('Enter your name: ')
            age = int(input('Enter your age: '))
            address = input('Enter your address: ')
            balance = float(input('Enter your current balance: '))
            account_number = int(input('Enter your 7 digit account number: '))
            PIN_number = int(input('Enter your PIN number: '))
            customer = customer_account(name,age,address,balance,account_number,PIN_number)
            customers.append(customer)
        elif int(num)==2:
            account_num= int(input('Enter your account number: '))
            PIN_num= int(input('Enter your PIN number: '))
            customer_account.login(account_num,PIN_num)
    
        

        

            
John = ('John',32,'1 London Road',209,2022,3333)
Robyn = ('Robyn',22,'129 Ashley Road',900,7862,0000)      
main()
print(customers)