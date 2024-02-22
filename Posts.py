# import matplotlib.pyplot as plt
from builtins import list
from enum import Enum

import SocialNetwork
# import Users


class PostType(Enum):
    TEXT = "Text"
    IMAGE = "Image"
    SALE = "Sale"

    """
        Factory method to create different types of posts based on the given type.

        Args:
            p_type (str): Type of the post.
            owner (object): Owner of the post.
            *args: Additional arguments based on the post type.

        Returns:
            Post: An instance of the corresponding post type.
        """


class PostsFactory:
    @staticmethod
    def create_post(p_type: str, owner, *args):
        if p_type == PostType.TEXT.value:
            return TextPost(owner, *args)
        elif p_type == PostType.IMAGE.value:
            return ImagePost(owner, *args)
        elif p_type == PostType.SALE.value:
            return SalePost(owner, *args)


class Post:
    likes = set()
    comments = list()
    owner = ''

    """
           Initialize a post object.

           Args:
               owner (object): The owner of the post.
           """
    def __init__(self, owner):
        self.owner = owner

    """
           Method to handle liking a post.

           Args:
               user (object): The user who is liking the post.
           """
    def like(self, user):
        net = SocialNetwork.SocialNetwork("")
        if net.is_online(user.name):
            self.likes.add(user.name)
            if self.owner != user:
                notification_message = f"{user.name} liked your post"
                # print(notification_message)
                self.owner.update("Like", user, notification_message)
        return

    """
            Method to handle commenting on a post.

            Args:
                user (object): The user who is commenting on the post.
                desc (str): The comment content.
            """
    def comment(self, user, desc):
        net = SocialNetwork.SocialNetwork("")
        if net.is_online(user.name):
            self.comments.append((user, desc))
            if self.owner.name != user.name:
                self.owner.update("Comment", user, desc)
        return

    """
            Generate a string representation of the post.

            Returns:
                str: The string representation of the post.
            """

    def __post_as_string(self):
        pass

    """
           Print the post.
           """
    def print(self):
        pass


# Concrete implementation of a Text Post.
class TextPost(Post):
    content = ""

    def __init__(self, owner, content):
        super().__init__(owner)
        self.content = content
        self.print()
        msg = self.__post_as_string()
        owner.notify("Post", msg)

    def print(self):
        print(self.__post_as_string())

    def __post_as_string(self):
        return f"{self.owner.name} published a post:\n\"{self.content}\"\n"

    def __str__(self):
        return self.__post_as_string()


# Concrete implementation of an Image Post.
class ImagePost(Post):
    image_url = ""

    def __init__(self, owner, image_url):
        super().__init__(owner)
        self.image_url = image_url
        self.print()
        msg = self.__post_as_string()
        owner.notify("Post", msg)

    def display(self):
        try:
            # plt.imshow(self.image_url)
            print("Shows picture")
        except FileNotFoundError:
            print("No image found")
        return

    def print(self):
        print(self.__post_as_string())

    def __post_as_string(self):
        return f"{self.owner.name} posted a picture\n"

    def __str__(self):
        return self.__post_as_string()


# Concrete implementation of a Sale Post.
class SalePost(Post):
    text = ""
    price = 0.0
    location = ""
    is_sold = False
    amountOfDiscount = 0.0

    def __init__(self, owner, *args):
        super().__init__(owner)
        text, price, location = args
        self.text = text
        self.price = float(price)
        self.location = location
        self.is_sold = False
        self.print()
        self.owner.notify("Post", self.__post_as_string())

    def discount(self, amount_of_discount, password):
        if self.owner.correct_password(password):
            self.price = self.price * (1 - amount_of_discount / 100)
            msg = f"Discount on {self.owner.name} product! the new price is: {self.price}"
            print(msg)
            # self.owner.notify(msg)
        return self

    def sold(self, password):
        if self.owner.correct_password(password):
            self.is_sold = True
            print(f"{self.owner.name}'s product is sold")
        return

    def print(self):
        print(self.__post_as_string())

    def __str__(self):
        return self.__post_as_string()

    def __post_as_string(self):
        sold_text = "Sold!" if self.is_sold else "For sale!"
        price_update = self.price if self.is_sold else int(self.price)
        msg = f"{self.owner.name} posted a product for sale:\n"
        msg = msg + f"{sold_text} {self.text}, price: {price_update}, pickup from: {self.location}\n"
        return msg
