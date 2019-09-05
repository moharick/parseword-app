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
