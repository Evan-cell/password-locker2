import random
from user import user

def create_user(user_name, password):
    '''
    Function to create a new user
    '''
    new_user = user(user_name, password)
    return new_user
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()
    
def main():
    
    while True:
        print("welcome to password vault")
        print('\n')  
        print("please select a shortcode to navigate through:'nu' to create a new accout 'lg' to login 'ex' to exit the application")  
        shote_code = print()