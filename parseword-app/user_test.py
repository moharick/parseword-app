import unittest #unittest module imported
from user import User #Importing class User from module user

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.test_user = User("moha", "moharick", "gfTah2")

    def test_init(self):
          '''
          test_init test case to test if the object is initialized properly
          '''
          self.assertEqual(self.test_user.username, "moharick")
          self.assertEqual(self.test_user.name, "moha")
          self.assertEqual(self.test_user.password, "gfTah2")

if __name__ == '__main__':
    unittest.main()
