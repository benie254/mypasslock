import unittest #unittest module
from account import Account #account class


class TestAccount(unittest.TestCase):
    
    '''
    To define test cases for the pass account's behaviors
    '''
    
    def setUp(self):
        
        '''
        The Set up method--required at the initialization of tests
        '''
        
        self.new_account = Account('Twitter', 'benie@gmail.com', '0708646667', 'benie','mypassword')