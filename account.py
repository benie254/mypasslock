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
        
        for account in cls.account_details:
            if account.account_name == id:
                return account
            
    
    @classmethod
    def account_exist(cls,id):
        
        '''
        Method--checks if object exists by taking in its name
        '''
        
        for account in cls.account_details:
            if account.account_name == id:
                return True

        return False
    
    
    @classmethod
    def display_accounts(cls):
        
        '''
        Method--returns all saved objects from the list
        '''
        
        return cls.account_details