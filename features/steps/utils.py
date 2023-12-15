# Some important util things go in here, usually functionality used in several step classes...

class UserProvider(object):

    def __init__(self):
        self.sth = "sth"

    def get_user(self, options):

        # Based on options get appropriate user from data source

        user = {
            "username": "test1",
            "password": "1234",
            "email": "test1@example.org",
        }
        return user
