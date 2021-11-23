#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:21:36 2021

@author: jackmather

This file contains the Online Bank class. This class manages customers' 
accounts. Online bank can:
Process money transfer among customers
Logout the system safely
"""
from Customer_Account_Class import customer_account

class online_bank(customer_account):
    def __init__(self,name,age,gender,address,balance,account_number,PIN):
        super().__init__(name,age,gender,address,balance,account_number,PIN)
    def logout(self):
        print('Logged out successfully!')
    def process_transfer(self,)