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
def delete_account(account):
    
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
                    save_new_password(create_new_password(credent_user,credent_pass))
                    break
                elif users_code == 'G':
                    credent_pass = generate_password()
                    print()
                    print(f'Account creation successful. Your generated password is: {credent_pass} \
                        Keep it safe for future reference.')
                    print('-'*10)
                    save_new_password(create_new_password(credent_user,credent_pass))
                    break
                else:
                    print('-'*10)
                    print('Please try again!')
                    
        else:
            while True:
                print('-' * 5)
                print()
                print("Didn't quite get that. Use the short codes...")
                print()
                print('-' * 5)
                break
            
    
    #Pass locker home page  
    
    while True:
        
        print("Use these short codes:")
        print('-'*5)
        print(" se - save existing acc, ca - create new acc, da - display accs, fa - find acc, del - delete acc, ex - exit")
        print()

        short_code = input().lower() 
        if short_code == 'se':
            print()
            
            #add existing account 
            print('Add Existing Account')
            print()
            print('-'*10)
                    
            print()
            print('Account name ...')
            print()
            ex_acc_name = input()
            print()
            print('-'*10)
                    
            print()
            print('Username ...')
            print()
            ex_acc_user = input()
            print()
            print('-'*10)
                    
            print()
            print('Password')
            print()
            ex_acc_pass = input()
            print()
            print()
            print('-'*10)
                    
            print()
            print('Email--if relevant')
            print()
            ex_acc_email = input()
            print()
            print('-'*10)
                    
            print()
            print('Phone number--if relevant')
            print()
            ex_acc_phone = input()
            print()
            print('-'*10)
                    
                    
            save_existing_accounts(existing_account(ex_acc_name,ex_acc_email,ex_acc_phone,ex_acc_user,ex_acc_pass))
                    
            print('\n')
            print(f'Existing Pass_Account {ex_acc_name} for username: {ex_acc_user} saved')
            print('\n')
            
        elif short_code == 'ca':
            print()
            
            #Create new pass account
            print('New Pass_Account')
            print('-'*10)

            print()
            print('Account ...')
            print()
            acc_name = input()
            print()
            print('-'*10)

            print()
            print('Email ...')
            print()
            acc_email = input()
            print()
            print('-'*10)
                    

            print()
            print('Phone number ...')
            print()
            p_number = input()
            print()
            print('-'*10)

            print()
            print('Username ...')
            print()
            acc_user = input()
            print()
            print('-'*10)
            
            print()
            print('Password ...')
            print()
               
            #offer users an option to create a new password or generate one     
            while True:
                print('Enter CP to Create a pass_account password ...\
                        Enter GP to Generate a pass_account password')
                print()
                print('-'*10)
                pass_code = input().upper()
                if pass_code == 'CP':
                    print()
                    print('Create New Password')
                    print()
                    acc_pass = input()
                    print('-'*10)
                    print()
                    print(f'Your new password is: {acc_pass}')
                    print()
                    print('-'*10)
                    
                    save_new_accounts(create_new_account(acc_name,acc_email,p_number,acc_user,acc_pass))
                    break
                elif pass_code == 'GP':
                    acc_pass = generate_password()
                    print()
                    print(f'Your generated password is: {acc_pass}')
                    print('-'*10)
                    
                    save_new_accounts(create_new_account(acc_name,acc_email,p_number,acc_user,acc_pass))
                    break
                else:
                    print('-'*10)
                    print()
                    print("Didn't quite get that. Please use the short codes.")
                    print()
                                    
                    
            print('\n')
            print(f'New Pass_Account {acc_name} for username: {acc_user} created')
            print('\n')
            
        elif short_code == 'da':
            
            #display all accounts
            if display_accounts():
                print('-'*10)
                print()
                print('Here is a list of all your pass_accounts')
                print('\n')
                

                for pass_account in display_accounts():
                    print(f'{pass_account.account} {pass_account.email} ...... {pass_account.username}')
                    print ('\n')
                    print('-'*10)
            
            else:
                    print('-'*10)
                    print('\n')
                    print("You don't seem to have any pass_accounts saved yet.")
                    print('\n')
                    print('-'*10)
        
        elif short_code == 'fa':
            
            #search saved account
            print('-'*10)
            print()
            print('Enter the account you want to search for: ')
            print()
            print('-'*10)

            print()
            search_id = input()
            if check_existing_accounts(search_id):
                search_account = find_account(search_id)
                print(f'{search_account.account}')
                print('-' * 10)
                        
                print()
                print(f'Email ...... {search_account.email}')
                print(f'Phone number ...... {search_account.phone_number}')
                print(f'Username ...... {search_account.username}')
                print(f'Password ...... {search_account.password}')
                print('\n')
            
            else:
                print('-'*10)
                print()
                print('That pass_account does not exist')
                print()
                print('-'*10)
                
        elif short_code == 'del':
             
             #delete a saved account       
            print('-'*10)
            print()
            print('Enter the account you want to delete: ')
            print()
            print('-'*10)
                    
            del_id = input().lower()
            print()
            while True:
                print(f'Are you sure you want to delete this pass account? *** y (for YES) / n (for NO)')
                print()
                print('-'*10)
                user_code = input()
                if user_code == 'y':
                    if find_account(del_id):
                        search_account = find_account(del_id)
                        search_account.delete_account()
                        
                        print('-'*10)
                        print()
                        print(f"Your pass_account {search_account.account} has been deleted")
                        print()
                        
                        print('-'*10)
                        print()
                        break
                    
                    else:
                        print('-'*10)
                        print()
                        print('Sorry! Account does not exist')
                        print()
                        print('-'*10)
                        break
                elif user_code == 'n':
                    print('-'*10)
                    print()
                    print('Account will not be deleted')
                    print()
                    print('-'*10)
                    break
                else:
                    print('-'*10)
                    print()
                    print("Didn't quite get that. Please use the short codes!")
                    print()
                    print('-'*10) 
        
        #exit pass locker
        elif short_code == 'ex':

            print('-'*10)
            print('\n')
            print('Bye ......')
            print('\n')
            print('-'*10)
            break
        else:
            print('-'*10)
            print('\n')
            print("Didn't quite get that. Please use the short codes.")
            print('\n')
            print('-'*10)
    

if __name__ == '__main__':
    main()