class User:
    """
    Class that generates new users.
    """

    userList = []

    def __init__(self, name, username, password):
        self.username = username
        self.name = name
        self.password = password

    def save_user(self):
        '''
        function that saves User objects into userList
        '''
        self.userList.append(self)



