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
        
    
    def test_init(self):
        
        '''
        Object initialization test case--test_init
        '''
        
        self.assertEqual(self.new_pass.lock_user,'janja')
        self.assertEqual(self.new_pass.lock_pass,'pass123')
        
    
    def test_save_new_password(self):
        
        '''
        To test if password object is saved into the login credentials list
        '''
        
        self.new_pass.save_new_password()
        self.assertEqual(len(Password.login_details),1)