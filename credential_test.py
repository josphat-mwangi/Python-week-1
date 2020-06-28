import unittest
from credential import Card


class TestCard(unittest.TestCase):
    '''
    Test class that defines test cases for the card class credetials.
    '''

    def setup(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_card = Card("Tom Jino", "KCB", "tomjino@gmail.com")

    def test_init(self):
        self.assertEqual(self.new_card.username, "Tom Jino")
        self.assertEqual(self.new_card.accounts, "KCB")
        self.assertEqual(self.new_card.email, "tomjino@gmail.com")


if __name__ == '__main__':
    unittest.main()
