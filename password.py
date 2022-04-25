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