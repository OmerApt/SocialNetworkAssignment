'''we need to add here singleton'''


class SocialNetwork:
    name = ""
    _instance = None





    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super.__new__(cls)
            cls._instance = name
            # create fields for class
        return cls._instance

    def sign_up(self, name, password):
        v = ""

    def log_in(self, name, password):
        v = ""

    def log_out(self, name):
        z = " "


def SocialNetwork(name):
    return
