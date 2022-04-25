import random #random module


class Password:
    
    """
    To generate new instances of passwords.
    """
    
    
    login_details = [] #empty login credentials list
    
    
    def save_password(self):
        
        '''
        Method--saves login credentials to credentialslist
        '''
        
        Password.login_details.append(self)
        
        
    def __init__(self,lock_user,lock_pass):
        
        '''
        To define properties of login credentials objects
        '''
        
        self.lock_user = lock_user
        self.lock_pass = lock_pass