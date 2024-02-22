from abc import ABC, abstractmethod

# from Posts import Post
import Posts
import SocialNetwork


class User:
    def __init__(self, name):
        self.followers = list()
        self.notifications = list()
        self.name = name
        self.posts_num = 0

    def __eq__(self, other):
        return self.name == other.name

    def __cmp__(self, other):
        return self.name == other.name

    def notify(self, msg,to_print):
        for follower in self.followers:
            follower.update(msg, to_print)
        return

    def update(self, message, to_print):
        notification = f"notification to {self.name}: {message}"
        self.notifications.append(notification)
        if to_print:
            print(notification)

    def add_follower(self, follower):
        if follower not in self.followers:
            self.followers.append(follower)

    def remove_follower(self, follower):
        if follower in self.followers:
            self.followers.remove(follower)

    def follow(self, followee):
        followee.add_follower(self)
        s = self.name + " started following " + followee.name
        print(s)
        return

    def unfollow(self, followee):
        followee.remove_follower(self)
        s = followee.name + " unfollowed " + self.name
        print(s)
        return

    def publish_post(self, post_type, *args):
        pf = Posts.PostsFactory()
        p = pf.create_post(post_type, self, *args)
        # self.notify()
        self.posts_num += 1
        # print()
        return p

    def print_notifications(self):
        for notification in self.notifications:
            print(notification)

    def correct_password(self, password):
        net = SocialNetwork.SocialNetwork("")
        psw = net.allUsers.get(self.name)[1]
        return psw == password


class Member(ABC):

    @abstractmethod
    def update(self, newsletter):
        pass
