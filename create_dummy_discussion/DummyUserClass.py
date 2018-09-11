from .fetch_api import get_access_token

class DummyUser():
    def __init__(self, name):
       self.name = name
       self.password = "test"
       self.token = get_access_token(self.name,self.password)