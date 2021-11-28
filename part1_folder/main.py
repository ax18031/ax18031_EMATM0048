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
            customer = customer_account(name=name,age=age,address=address,balance=balance,PIN=PIN)
            customer.create_account()         
        break


main()

        


