import Users

"""
Represents a social network system.

This class implements the Singleton Design Pattern, ensuring that only one instance
of the social network can exist throughout the program execution.

Attributes:
    name (str): The name of the social network.
    _instance (SocialNetwork): The single instance of the SocialNetwork class.
    allUsers (dict): A dictionary containing all registered users in the social network.
    logged_in (list): A list of usernames currently logged into the social network.
"""


class SocialNetwork(object):
    """
       Represents a social network system.

       This class implements the Singleton Design Pattern, ensuring that only one instance
       of the social network can exist throughout the program execution.

       Attributes:
           name (str): The name of the social network.
           _instance (SocialNetwork): The single instance of the SocialNetwork class.
           allUsers (dict): A dictionary containing all registered users in the social network.
           logged_in (list): A list of usernames currently logged into the social network.
       """
    name = ""
    _instance = None  # Single instance of the SocialNetwork class
    allUsers = dict()  # Dictionary to store all registered users

    def __new__(cls, name):
        """
        Create a new instance of the SocialNetwork class if it does not already exist.

        This method overrides the __new__ method of the object class to enforce the Singleton pattern.
        It ensures that only one instance of the SocialNetwork class is created.

        Args:
            name (str): The name of the social network.

        Returns:
            SocialNetwork: The single instance of the SocialNetwork class.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = name
            cls._instance.logged_in = list()
            print(f"The social network {cls._instance.name} was created!")
            # create fields for class
        return cls._instance

    def sign_up(self, name, password):
        """
        Register a new user in the social network.

        Args:
            name (str): The username of the new user.
            password (str): The password chosen by the new user.
        """
        if self.good_password(password) and not self.is_name_exists(name):
            usr = Users.User(name)
            self.allUsers[name] = (usr, password)
            self.logged_in.append(name)
            return usr
        return None

    # Check if a username already exists in the social network.
    def is_name_exists(self, name):
        return self.allUsers.get(name) is not None

    def good_password(self, password):
        """
       Check if a password meets the requirements.
       Args:
           password (str): The password to check.
       """
        size = len(password)
        if 4 <= size <= 8:
            return True

        return False

    # Check if a user is currently logged into the social network.
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
                    print(f"{name} connected")

    def log_out(self, name):
        if name in self.logged_in:
            self.logged_in.remove(name)
            print(f"{name} disconnected")

    # Return a string representation of the social network.
    def __str__(self):
        prt = ""
        num = 0
        for name, unp in self.allUsers.items():
            if num != 0:
                prt += "\n"
            else:
                num = 1
            user = unp[0]
            prt += f"{user}"
        return prt
