import random #random module


class Password:
    
    """
    To generate new instances of passwords.
    """
    
    
    login_details = [] #empty login credentials list
    
    
    def save_new_password(self):
        
        '''
        Method--saves login credentials to credentials list
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
            
    
    @classmethod
    def find_user_by_id(cls,id):
        
        '''
        Method--takes in username and finds it from the credentials list
        '''
        
        for password in cls.login_details:
            if password.lock_user == id:
                return password
            
    
    @classmethod
    def pass_exist(cls,id):
        
        '''
        Method--checks if input password exists in credentials list
        '''
        
        for account_password in cls.login_details:
            if account_password.lock_pass == id:
                return True

        return False
    
    
    @classmethod
    def user_exist(cls,id):
        
        '''
        Method--checks if input user exists in credentials list
        '''
        
        for password in cls.login_details:
            if password.lock_user == id:
                return True

        return False
    
    
    @classmethod
    def generate_password(self):
        
        '''
        Method--generates a random password
        '''
        
        my_combo = (''.join(chr(random.randrange(65,90)) for i in range(1))).lower()
        my_combo2 = ''.join(chr(random.randrange(65,90)) for i in range(2))
        my_combo3 = ''.join(chr(random.randrange(65,90)) for i in range(1)).lower()
        combo_2 = my_combo3 + my_combo2 + my_combo
        my_rand = random.randint(1000,9999)
        random_pass = '@' + combo_2 + str(my_rand) + '?!'
        
        return(random_pass)