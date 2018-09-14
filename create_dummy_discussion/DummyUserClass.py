import fetch_api


class DummyUser():
    def __init__(self, name):
        self.name = name
        self.password = "test"
        self.token = fetch_api.get_access_token(self.name, self.password)
