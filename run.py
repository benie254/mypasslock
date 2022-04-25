#!/usr/bin/env python

from account import Account
from password import Password

account_details = []


#create an account
def create_account(acc,email,phone,user,password):

    new_account = Account(acc,email,phone,user,password)
    return new_account


#add an existing account
def existing_account(ex_acc,ex_email,ex_phone,ex_user,ex_password):

    existing_account = Account(ex_acc,ex_email,ex_phone,ex_user,ex_password)
    return existing_account


#create the account login password
def create_account_password(credent_user,credent_pass):
    
    new_pass = Password(credent_user,credent_pass)
    return new_pass


#save new accounts
def save_new_accounts(account):

    account.save_new_account()
    

#save existing accounts
def save_existing_accounts(account):

    account.save_existing_account()