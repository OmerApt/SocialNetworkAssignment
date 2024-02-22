'''we need to add here singleton'''
import Users


class SocialNetwork(object):
    name = ""
    _instance = None
    allUsers = dict()

    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = name
            cls._instance.logged_in = list()
            print(f"The social network {cls._instance.name} was created!")
            # create fields for class
        return cls._instance

    def sign_up(self, name, password):

        if self.good_password(password) and not self.is_name_exists(name):
            usr = Users.User(name)
            self.allUsers[name] = (usr, password)
            self.logged_in.append(name)
            return usr
        return None

    def is_name_exists(self, name):
        return self.allUsers.get(name) is not None

    def good_password(self, password):
        size = len(password)
        if 4 <= size <= 8:
            return True

        return False

    def is_online(self, user_name):
        for user in self.logged_in:
            if user_name == user:
                return True
        return False

    def log_in(self, name, password):
        user_and_password = self.allUsers.get(name)
        if user_and_password is not None:
            usr_password = user_and_password[1]
            if usr_password == password:
                if name not in self.logged_in:
                    self.logged_in.append(name)
                    pri

    def log_out(self, name):
        if name in self.logged_in:
            self.logged_in.remove(name)
