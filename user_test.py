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

    def tearDown(self):
        '''
        teardone method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is intialized properly
        '''
        self.assertEqual(self.new_user.first_name, "Jopa")
        self.assertEqual(self.new_user.last_name, "Mwangi")
        self.assertEqual(self.new_user.password, "Nevergiveup")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved to the user list

        '''

        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.user_list), 1)

    def test_delete_user(self):
        '''
        test_delete_user is a test case to test if user object can be removed from user list
        '''
        self.new_user.save_user()
        self.new_user.delete_user()  # delete user object
        self.assertEqual(len(User.user_list), 0)


if __name__ == '__main__':
    unittest.main()
