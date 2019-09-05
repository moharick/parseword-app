from pyfiglet import Figlet
import random
import string
import emoji
from user import User
from credentials import Credential

userList = []


def __init__(self, name, username, password):
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

        for user in userList:
            if loginUsername == user[0] and loginPassword == user[1]:
                print("Welcome " + loginUsername)
                print("Hi, " + loginUsername + " please enter")
                while True:
                    print("*"*70)
                    print(loginUsername + " ,select an option")
                    print("1. View sites")
                    print("2. Add site")
                    print("3. Delete site")
                    print("4. Back")
                    option = int(input())
                    if option == 1:
                        print("Here are the sites added")
                        print(Credential.apps)
                    elif option == 2:
                        print("Enter site name:")
                        name = input()
                        print("Enter your username in the site above")
                        username = input()
                        print(
                            "Would you like to create or generate a password for " + name + "?")
                        print("1. Create password")
                        print("2. Generate password ")
                        app_option_selected = int(input())
                        if app_option_selected == 1:
                            print("Enter password below")
                            password = input()
                            Credential.apps.append(
                                [name, username, password])
                        elif app_option_selected == 2:
                            generator = passGen()
                            Credential.apps.append(
                                [name, username, generator])
                        print("Site succesfully added")
                    elif option == 3:
                        del_site = input('Enter the site to delete')
                        credentials.del_app()
                    elif option == 4:
                        break

            else:
                print("This user does not exist, kindly register")

    elif option_selected == 2:
        print("*"*70)
        print("Welcome" + " " + (emoji.emojize(":grinning_face_with_big_eyes:")
                                 ) + " " + (emoji.emojize(":grinning_face_with_big_eyes:")))
        print(" Create your username:")
        newUsername = input()
        print("Please select an option")
        print("1. Create password")
        print("2. Generate password ")
        print("3. Quit ")
        newPassword = int(input())

        if newPassword == 1:
            print("Enter password")
            newPassword = input()
            userList.append([newUsername, newPassword])

        elif newPassword == 2:
            generator = passGen()
            print(generator)
            userList.append([newUsername, generator])
    elif option_selected == 3:
        while True:
            print("Do you wish to delete?")

    else:
        break
