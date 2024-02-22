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

    def notify(self, action, message):
        for follower in self.followers:
            follower.update(action, self, message)
        return

    def update(self, action, sender, msg):
        notification = ""
        if action == "Post":
            notification = f"{sender.name} has a new post"
            # print(f"notification to {self.name}: {notification}")
        elif action == "Like":
            notification = f"{sender.name} liked your post"
            print(f"notification to {self.name}: {notification}")
        elif action == "Comment":
            notification = f"{sender.name} commented on your post"
            print(f"notification to {self.name}: {notification}: {msg}")
        self.notifications.append(notification)

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
        s = self.name + " unfollowed " + followee.name
        print(s)
        return

    def publish_post(self, post_type, *args):
        p = Posts.PostsFactory.create_post(post_type, self, *args)
        # self.notify()
        self.posts_num += 1
        # print()
        return p

    def print_notifications(self):
        print(f"{self.name}'s notifications:")
        for notification in self.notifications:
            print(notification)

    def correct_password(self, password):
        net = SocialNetwork.SocialNetwork("")
        psw = net.allUsers.get(self.name)[1]
        return psw == password

    def __str__(self):
        return (f"User name: {self.name}, Number of posts: {self.posts_num}, "
                f"Number of followers: {len(self.followers)}")


class Member(ABC):

    @abstractmethod
    def update(self, newsletter):
        pass
