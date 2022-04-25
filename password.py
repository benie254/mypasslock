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
        
        
    @classmethod
    def find_pass_by_id(cls,id):
        
        '''
        Method--takes in password input and finds it from the credentials list
        '''
        
        for password in cls.login_details:
            if password.lock_pass == id:
                return password