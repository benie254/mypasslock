#!/usr/bin/env python

from account import Account
from password import Password

account_details = []


#create an account
def create_new_account(acc,email,phone,user,password):

    new_account = Account(acc,email,phone,user,password)
    return new_account


#add an existing account
def existing_account(ex_acc,ex_email,ex_phone,ex_user,ex_password):

    existing_account = Account(ex_acc,ex_email,ex_phone,ex_user,ex_password)
    return existing_account


#create the account login password
def create_new_password(credent_user,credent_pass):
    
    new_pass = Password(credent_user,credent_pass)
    return new_pass


#save new accounts
def save_new_accounts(account):

    account.save_new_account()
    

#save existing accounts
def save_existing_accounts(account):

    account.save_existing_account()
    

#save login password    
def save_new_password(password):
    
    password.save_new_password()
    
    
#finding an account
def find_account(id):

    return Account.find_by_id(id)


#find a password
def find_pass(id):

    return Password.find_pass_by_id(id)


#find a passlock user
def find_user(id):
    
    return Password.find_user_by_id(id)


#check if account exists
def check_existing_accounts(id):

    return Account.account_exist(id)


#check if login password is correct
def check_existing_pass(id):

    return Password.pass_exist(id)


#check if login user exists
def check_existing_user(id):

    return Password.user_exist(id)


#display all accounts
def display_accounts():

    return Account.display_accounts()


#delete account
def delete_account(pass_account):
    
    return Account.delete_account()


#generate random password
def generate_password():
    
    generate_pass = Password.generate_password()
    return generate_pass


#call all methods
def main():
    

if __name__ = '__main__':
    main()