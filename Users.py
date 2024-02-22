from abc import ABC, abstractmethod

# Importing necessary modules
import Posts
import SocialNetwork


class User:
    """
    Represents a user in the social network.

    Attributes:
        name (str): The name of the user.
        followers (list): A list of users who follow this user.
        notifications (list): A list of notifications received by the user.
        posts_num (int): The number of posts published by the user.
    """
    def __init__(self, name):
        self.followers = list()
        self.notifications = list()
        self.name = name
        self.posts_num = 0

    def __eq__(self, other):
        return self.name == other.name

    def __cmp__(self, other):
        return self.name == other.name

    def notify(self, action: str, message: str):
        """
        Notifies followers about a user action.

        This method acts as the subject (observable) in the Observer Pattern.
        It broadcasts notifications to all followers (observers) when the user performs an action
        such as posting, liking, or commenting.

        Args:
            action (str): The type of action (e.g., post, like, comment).
            message (str): The message to be notified.
        """

        for follower in self.followers:
            follower.update(action, self, message)
        return

    def update(self, action: str, sender, msg: str):
        """
        Update user with notifications based on actions from others (e.g., post, like, comment).

        This method acts as the observer's callback in response to notifications.
        It allows followers (observers) to react accordingly to actions performed by others,
        such as receiving new posts, likes, or comments.

        Args:
            :param action :Type of action.
            :param sender : User who initiated the action.
            :param msg : Message associated with the action.

        """

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
        """
        Publish a post by creating an instance of the specified post type.

        Args:
            post_type (str): Type of the post.
            *args: Additional arguments required for post creation.

        Returns:
            Post: The created post object.
        """
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
        """
        Check if the provided password is correct for the user.

        Args:
            password (str): Password to be checked.

        Returns:
            bool: True if the password is correct, False otherwise.
        """

        net = SocialNetwork.SocialNetwork("")
        psw = net.allUsers.get(self.name)[1]
        return psw == password

    def __str__(self):
        return (f"User name: {self.name}, Number of posts: {self.posts_num}, "
                f"Number of followers: {len(self.followers)}")


class Member(ABC):

    @abstractmethod
    def update(self, newsletter):
        """
        Abstract method for updating members with newsletters.

        Args:
            newsletter (str): The newsletter to be updated with.
        """
        pass
