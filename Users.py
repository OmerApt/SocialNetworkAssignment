from Posts import Post, TextPostFactory


class User:
    notifications = {}
    followers = {}
    posts_num = 0
    __password = " "

    def __init__(self, password):
        self.__password = password

    def notify(self):
        return

    def follow(self, name):
        return

    def unfollow(self, name):
        return

    def publish_post(self, type, content):
        if (type == "Text"):
            p = TextPostFactory.make_post(content)

        self.notify()
        self.posts_num += 1
        return

    def publish_post(self, sale, desc, price, location):
        return

    def print_notifications(self):
        return

    def correct_password(self, password):
        if self.__password == password:
            return True
        else:
            return False
