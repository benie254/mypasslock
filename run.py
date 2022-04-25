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
    
    #welcome section
    print('\n')
    print("Welcome to your pass_account!")
    print('\n')
    
    #short codes to begin
    while True:
        print('Type lg to LOG IN \
            \
            Type cr to CREATE a new account ')
        print()
        
        first_code = input().lower()
        
        #Account login section--log in to passlock
        if first_code == 'lg':
            print()
            print('Account Log In')
            print('-'*10)
            
            #enter existing passlock username--check if user exists
            while True:
                
                print('Enter your PassLock username ... :')
                print()
                user_id = input()
                if check_existing_user(user_id):
                    search_user = find_user(user_id)
                    print(f'{search_user.lock_user}')
                    print('-' * 20)
                        
                    print(f'One more thing, {search_user.lock_user}!')
                    print()
                    break
                else:
                    print()
                    print('Sorry! User does not exist.\
                        Enter an existing username\
                            Or press CTR + Z to exit')
                    print()
                    
            
            #enter existing password--check if it is correct
            
            while True:
                print('Enter your PassLock password ... :')
                print()
                pass_id = input()
                if check_existing_pass(pass_id):
                    search_pass = find_pass(pass_id)
                    print(f'{search_pass.lock_pass}')
                    print('-' * 20)
                        
                    print(f'Login successful ...... You are in.')
                    print('\n')
                    print(f"Hello, {credent_user}. This is your PassLock account. Wanna have a look around?")
                    print('\n')
                    break
                else:
                    print('-' * 10)
                    print()
                    print(f'Wrong password for account username {credent_user}. \
                    Please try again\
                        Or press CTRL + Z to exit')
                    print()
                    print('-' * 10)
            break
        
        #Account sign up section--create passlock account
        
        elif first_code == 'cr':
            
            print('-'*5)
            print()
            print('Account Sign Up')
            print()
            
            #create passlock username--checks if it already exists
            print('Create a PassLock username ...')
            print()
            print('-'*5)
            print()
            
            
            while True:
                
                
                credent_user = input()
                print()
            
                print('-'*5)
                
                if check_existing_user(credent_user):
                    search_user = find_user(credent_user)
                    print()
                    print(f'Username {search_user.lock_user} exists! \
                        Please create a unique username\
                        Or press CTRL + Z to exit.')
                    print()
                else:
                    print()
                    print(f'One more thing, {credent_user}! \
                        Create a password')
                    print()
                    break
            
            #create passlock password  
            while True:
                print('Enter C to Create a PassLock password ...\
                    Enter G to Generate a PassLock password')
                print()
                print('-'*10)
                users_code = input().upper()
                if users_code == 'C':
                    print()
                    print('Create New Password')
                    print()
                    credent_pass = input()
                    print('-'*10)
                    print()
                    print(f'Account creation successful. Your new password is: {credent_pass} \
                        Keep it safe for future reference')
                    print()
                    print('-'*10)
                    save_account_password(create_account_password(credent_user,credent_pass))
                    break
                elif users_code == 'G':
                    credent_pass = pass_gen()
                    print()
                    print(f'Account creation successful. Your generated password is: {credent_pass} \
                        Keep it safe for future reference.')
                    print('-'*10)
                    save_account_password(create_account_password(credent_user,credent_pass))
                    break
                else:
                    print('-'*10)
                    print('Please try again!')
    

if __name__ = '__main__':
    main()