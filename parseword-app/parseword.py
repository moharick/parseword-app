from pyfiglet import Figlet
import random
import string
import emoji
from user import User
from credentials import Credential
userList = []


def __init__(self, name, username, password):
    """
    Class that generates new users.
    """
    self.username = username
    self.name = name
    self.password = password


def del_app(credentials):
    '''
    Function to delete a credential
    '''
    credentials.del_app()

def passGen(size=8, char=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    gen = ''.join(random.choice(char) for _ in range(size))
    return gen