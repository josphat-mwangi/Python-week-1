#!/usr/bin/env python3.6
from user import User
from credential import Card


def create_user(fname, lname, password):
    '''
    Function to create a new user
    '''
    new_user = User(fname, lname, password)
    return new_user


def save_user(user):
    '''
    Function to save user

    '''
    user.save_user()


def del_user(user):
    '''
    Function to delete  users
    '''
    user.delete_user()


def create_card(username, accounts, email):
    '''
    Function to create a new card
    '''
    new_card = Card(username, accounts, email)
    return new_card


def save_cards(card):
    '''
    function to save card 

    '''
    card.save_card()


def del_card(card):
    '''
    function to delete a card 
    '''
    card.delete_card()


def displays_cards():
    '''
    Function that display all the cards save

    '''
    return Card.display_cards()


def main():
    print("Hello there welcome to Password locker.")
    print("")
    while True:
        print("Use these short codes : ca  - create new Account")
        short_code = input().lower()
        if short_code == 'ca':
            print("first name ..")
            fname = input()

            print("last name ..")
            lname = input()

            print("Password ...")
            password = input()

            save_user(create_user(fname, lname, password))
            print('\n')
            print(f"New User {fname} {lname} created")
            print('\n')
