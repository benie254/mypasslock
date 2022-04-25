import unittest #unittest module
from account import Account #account class


class TestAccount(unittest.TestCase):
    
    '''
    To define test cases for the pass account's behaviors
    '''
    
    
    def tearDown(self):
        
        '''
        Method--cleans up after tests--enables accurate test results
        '''
        
        Account.account_details = [] #empty list--to hold account details
    
    
    def setUp(self):
        
        '''
        The Set up method--required at the initialization of tests
        '''
        
        self.new_account = Account('Twitter', 'benie@gmail.com', '0708646667', 'benie','mypassword')
        
    
    def test_init(self):
        
        '''
        Object initialization test case--test_init
        '''
        
        self.assertEqual(self.new_account.account_name,'Twitter')
        self.assertEqual(self.new_account.email,'benie@gmail.com')
        self.assertEqual(self.new_account.phone_number,'0708646667')
        self.assertEqual(self.new_account.username,'benie')
        self.assertEqual(self.new_account.password,'mypass@123!')
        
    
    def test_save_new_account(self):
        
        '''
        To test if pass_account object is saved into the account details list
        '''
        
        self.new_account.save_new_account()
        self.assertEqual(len(Account.account_details),1)