'''we need to add here singleton'''
from Users import User


class SocialNetwork:
    name = ""
    _instance = None
    allUsers = dict()

    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super.__new__(cls)
            cls._instance.name = name

            # create fields for class
        return cls._instance

    def sign_up(self, name, password):

        if self.good_password(password) and not self.is_name_exists(name):
            usr = User(name)
            self.allUsers.update((usr, password))

            v = ""

    def is_name_exists(self, name):
        for usr, v in self.allUsers:
            if usr.name == name:
                return usr
            return False

    def good_password(self, password):
        size = len(password)
        if 4 <= size <= 8:
            return True

        return False

    def is_online(self, user):
        pass

    def log_in(self, name, password):
        if (name, password) in self.allUsers:
            v = ""

    def log_out(self, name):
        z = " "


def SocialNetwork(name):
    return
