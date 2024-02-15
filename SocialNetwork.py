'''we need to add here singleton'''


class SocialNetwork:
    name = ""
    _instance = None

    def __init__(self, name):
        self.name = name


    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance



    def sign_up(self, name, password):
        v = ""

    def log_in(self, name, password):
        v = ""

    def log_out(self, name):
        z = " "


def SocialNetwork(name):
    return
