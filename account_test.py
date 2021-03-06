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
        
        self.new_account = Account('Twitter', 'benie@gmail.com', '0708646667', 'benie','mypass@123!')
        
    
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
        To test if account object is saved into the account details list
        '''
        
        self.new_account.save_new_account()
        self.assertEqual(len(Account.account_details),1)
        
        
    def test_save_existing_account(self):
        
        '''
        To test if existing account object is saved in the account details list
        '''
        
        self.new_account.save_existing_account()
        self.assertEqual(len(Account.account_details),1)
        
        
    def test_save_multiple_account(self):
        
        '''
        To test if multiple objects can be saved into list--acount details
        '''
        
        self.new_account.save_new_account()
        test_account = Account("Test", "user@email.com", "0712345678", "user",'pass321$%')
        test_account.save_new_account()
        self.assertEqual(len(Account.account_details),2)
        
        
    def test_delete_account(self):
        
        '''
        To test if we can delete an account from the account details list
        '''
        
        self.new_account.save_new_account()
        test_account = Account("Test", "user@email.com", "0712345678", "user",'pass321$%')
        test_account.save_new_account()

        self.new_account.delete_account()
        self.assertEqual(len(Account.account_details),1)
        
        
    def test_find_account_by_id(self):
        
        '''
        To test if we can find an account by entering its name
        '''
        
        self.new_account.save_new_account()
        test_account = Account("Test", "user@email.com", "0712345678", "user",'pass321$%')
        test_account.save_new_account()

        found_account = Account.find_by_id('Test')

        self.assertEqual(found_account.account_name,test_account.account_name)
        
    
    def test_account_exists(self):
        
        '''
        To test if the account object exists in the account details list
        '''
        
        self.new_account.save_new_account()
        test_account = Account("Test", "user@email.com", "0712345678", "user",'pass321$%')
        test_account.save_new_account()

        account_exists = Account.account_exist("Test")

        self.assertTrue(account_exists)
        
    
    def test_display_all_accounts(self):
        
        '''
        To test if we can view all objects contained in the account details list
        '''
        
        self.assertEqual(Account.display_accounts(), Account.account_details)
        
        
if __name__ == '__main__':
    unittest.main()