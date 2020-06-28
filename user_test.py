import unittest
from user import User


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.Testcase:TestCase class that helps in creacting test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_user = User("Jopa", "Mwangi", "Nevergiveup")

    def test_init(self):
        '''
        test_init test case to test if the object is intialized properly
        '''
        self.assertEqual(self.new_user.first_name, "Jopa")
        self.assertEqual(self.new_user.last_name, "Mwangi")
        self.assertEqual(self.new_user.password, "Nevergiveup")
