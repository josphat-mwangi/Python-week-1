class Card:
    '''
    class for creating new intance

    '''
    card_list = []

    def __init__(self, username, accounts, email):
        '''
        __init__method helps define properties for our objects.

        '''
        self.username = username
        self.accounts = accounts
        self.email = email

    def save_card(self):
        '''
        method that save credebtials object to card list

        '''
        Card.card_list.append(self)
