class Credential:
    '''
    Class that generates new instances of user credentials for their accounts.
    '''
    apps = []
    user = []

    @classmethod
    def verify(cls, loginUsername, loginPassword):
        onlineUser = ''
        for user in user.userList:
            if (user.loginUsername == loginUsername and user.loginPassword == loginPassword):
                onlineUser = user.loginUsername
        return onlineUser

    @classmethod
    def delete_app(self):
        '''
        Class that deletes user credentials from their accounts.
        '''
        Credential.apps.remove(self)
