import random
from user import user

def create_user(user_name, password):
    '''
    Function to create a new contact
    '''
    new_user = user(user_name, password)
    return new_user