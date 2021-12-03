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
        customer_information = dict()
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
            account_numm= customer_account.account_number
            customer_information['Name'] = name
            customer_information['Age']=age
            customer_information['Address']=address
            customer_information['Balance']=balance
            customer_information['PIN']=PIN
            customer_information['Account Number']=account_numm
            customer = customer_account(name=name,age=age,address=address,balance=balance,PIN=PIN)
            customer.create_account()
        customers_= []
        customer_copy = customer_information.copy()
        customers_.append(customer_copy)
        break
        # elif int(num)==2:
            #"account_num = int(input('Please enter your account number: '))"
            #"pin = int(input('Please enter your 4 digit PIN: '))"


main()        




        


