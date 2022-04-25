class Account:
    
    """
    To generate new instances of pass_accounts.
    """
    
    account_details = [] #empty account details list
    
    
    def save_new_account(self):
        
        '''
        Method--saves new account details to the list
        '''
        
        Account.account_details.append(self)
        
    
    def __init__(self, account_name, email, phone_number, username, password):
        
        self.account_name = account_name
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.password = password