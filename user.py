class User:
    '''
    Class that generate new instances of user accounts.
    '''
    user_list = []  # empty user list

    def __init__(self, first_name, last_name, password):
        '''
            __init__ method that helps us define properties for our objects.

        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        save  user object in user_list

        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method that deletes saved user from the user_list
        '''
        User.user_list.remove(self)
