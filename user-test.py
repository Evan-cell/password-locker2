import unittest
from user import user

class Testuser(unittest.TestCase):
    
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = user("Evan","kimani","2021") # create contact object
def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Evan")
        
       
        self.assertEqual(self.new_user.password,"2021")
def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(user.user_list),1)        




if __name__ == '__main__':
    unittest.main()    