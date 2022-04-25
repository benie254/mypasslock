import unittest #unittest module
from password import Password #password class


class TestPassword(unittest.TestCase):
    
    '''
    To define test cases for the account password's behaviors
    '''
    
    
    def tearDown(self):
        
        '''
        Method--cleans up after tests--enables accurate test results
        '''
        
        Password.login_details = [] #empty login credentials list
        
    
    def setUp(self):
        
        '''
        The Set up method--required at the initialization of tests
        '''
        
        self.new_pass = Password('janja','pass123')