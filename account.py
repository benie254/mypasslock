class Account:
    
    """
    To generate new instances of pass_accounts.
    """
    
    account_details = [] #empty account details list
    
    def __init__(self, account, email, phone_number, username, password):
        
        self.account = account
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.password = password