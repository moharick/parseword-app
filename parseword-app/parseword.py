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
    '''function that generates random password
    '''

    return gen


custom_fig = Figlet(font='crawford')
print(custom_fig.renderText('PARSEWORD'))
print("*"*70)
print('Welcome to the Parseword App, where security is the key')
while True:
    print("Please select an option")
    print("1. Sign in ")
    print("2. Sign up ")
    print("3. Delete")
    print("4. Quit")
    option_selected = int(input())
if option_selected == 1:
    print("*"*70)
    print("Welcome" + " " + (emoji.emojize(":grinning_face_with_big_eyes:")
                             ) + " " + (emoji.emojize(":grinning_face_with_big_eyes:")))
    print("Please enter username:")
    loginUsername = input()
    print("Kindly enter password")
    loginPassword = input()
