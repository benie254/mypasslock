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
        
        
    def save_existing_account(self):
        
        '''
        Method--saves existing account details to the list
        '''
        
        Account.account_details.append(self)
        
    
    def __init__(self, account_name, email, phone_number, username, password):
        
        self.account_name = account_name
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.password = password
        
    
    def delete_account(self):
        
        '''
        Method--deletes account object
        '''
        
        Account.account_details.remove(self)
        
    
    @classmethod
    def find_by_id(cls,id):
        
        '''
        Method--takes in a list object's name and returns its details
        '''
        
        for pass_account in cls.account_details:
            if pass_account.account == id:
                return pass_account