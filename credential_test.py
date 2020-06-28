import unittest
from credential import Card


class TestCard(unittest.TestCase):
    '''
    Test class that defines test cases for the card class credetials.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_card = Card(
            "Jopa", "KCB", "jopa@gmail.com")

    def tearDown(self):
        '''
        teardone method that does clean up after each test case has run.
        '''
        Card.card_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is intialized properly
        '''
        self.assertEqual(self.new_card.username, "Jopa")
        self.assertEqual(self.new_card.accounts, "KCB")
        self.assertEqual(self.new_card.email, "jopa@gmail.com")

    def test_save_card(self):
        '''
        test_save_card test case to test if the user object is saved to the card list

        '''

        self.new_card.save_card()  # saving the new user
        self.assertEqual(len(Card.card_list), 1)

    def test_delete_card(self):
        '''
        test_delete_card is a test case to test if user object can be removed from card list
        '''
        self.new_card.save_card()
        self.new_card.delete_card()  # delete user object
        self.assertEqual(len(Card.card_list), 0)

    def test_display_all_cards(self):
        '''
        method that returns a list of all cards saved 

        '''
        self.assertEqual(Card.display_cards(), Card.card_list)


if __name__ == '__main__':
    unittest.main()
