#!/usr/bin/env python3.6
from user import User
from credential import Card
import random
import string


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


def generate_password(length=8):
    '''
    Function to generate a password
    '''
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(length))



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


def card_list():
    print("Hello there welcome to Password locker.")
    print("")
    
    while True:
        print("Use these short codes : CC - create new card DC - dispaly card  EX - exit")
        short_code = input().lower()
        if short_code == 'cc':
            print("New Card")

            print("Username ...")
            username = input()

            print("password")
            print(
                "Use the codes: \n gp - to generate a password \n cp - to create your own password")
            code = input().lower()
            if code == 'gp':
                password  = generate_password()
                print(password)
            elif code == 'cp':
                print("Password ....")
                password = input()
            else:
               print("Wrong short code. Please try again.")

            print("Email address ...")
            email = input()

            save_cards(create_card(username, password, email))

            print('/n')
            print(f"New Card {username} {password} {email} created")
            print('/n')
        elif short_code == 'dc':
            if displays_cards():
                print("Here is list of all cards")
                print('/n')

                for card in displays_cards():
                    print(f"{card.username} {card.email} {card.account}")
                    print('/n')
            else:
                print('/n')
                print("You dont seem to have any cards save ")
        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")


def main():
    print("Hello there welcome to Password locker.")
    print("")
    while True:
        print("Use these short codes : ca  - create new Account, su - login , ex - exit")
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
            print(f"Congratulations {fname}. Account created successfully!")
            print('\n')
            print("Kindly login!!!!!!!")
            print("Enter your first name...")
            f_name = input()
            print("Enter your last name...")
            l_name = input()
            print("Enter your Password...")
            p_name = input()

            if fname != f_name or lname != l_name or password != p_name:
                print("Invalid firstname lastname and password")

                print("Enter your first name...")
                f_name = input()
                print("Enter your last name...")
                l_name = input()
                print("Enter your Password...")
                p_name = input()
            else:
                print(
                    f"welcome {{f_name}} to password locker account."
                )

                card_list()
        elif short_code == "su":
            print("Enter firstname...")
            firstname = input()
            
            print("Enter password...")
            passwordname = input()

            if firstname != 'newuser' or passwordname != 'pass254':
                print("Account does not exist.Please create an account to login.")

            else:
                print("Hi, Welcome to your password locker account.")
                card_list()


        elif short_code == "ex":
            print("Bye ......")
            break
        else:
            print("Wrong short code. Please try again.")


                




        



   


if __name__ == '__main__':

    main()
