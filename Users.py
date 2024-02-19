from abc import ABC, abstractmethod

from Posts import Post, Post_type, PostsFactory

from SocialNetwork import SocialNetwork


class User:
    def __init__(self, name):
        self.followers = set()
        self.notifications = list()
        self.name = name
        self.posts_num = 0
        self._net = SocialNetwork("")

    def __eq__(self, other):
        return self.name == other.name

    def __cmp__(self, other):
        return self.name == other.name

    def notify(self,msg):
        for follower in self.followers:
            follower.update(msg)
        return

    def update(self,message):
        notification = f"notification to {self.name}: {message}"
        self.notifications.append(notification)

    def add_follower(self, follower):
        self.followers.add(follower)

    def remove_follower(self, follower):
        self.followers.remove(follower)

    def follow(self, followee):
        followee.add_follower(self)
        s = self.name + "started following " + followee.name
        print(s)
        return

    def unfollow(self, followee):
        followee.remove_follower(self)
        s = followee.name + "unfollowed " + self.name
        print(s)
        return

    def publish_post(self, type, *args):
        pf = PostsFactory()
        p = pf.create_post(type, args)
        # self.notify()
        self.posts_num += 1
        return p

    def print_notifications(self):
        for notification in self.notifications:
            print(notification)

    def correct_password(self, password):
        psw = self._net.allUsers.get(__key=self)
        return psw == password


class Member(ABC):

    @abstractmethod
    def update(self, newsletter):
        pass
