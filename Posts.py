import matplotlib.pyplot as plt
from builtins import list
from enum import Enum

import SocialNetwork
# from SocialNetwork import SocialNetwork
import SocialNetwork as sn
import Users


class PostType(Enum):
    TEXT = "Text"
    IMAGE = "Image"
    SALE = "Sale"


class PostsFactory:
    def create_post(self, p_type: {str}, owner, *args):
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

    def __init__(self, owner):
        self.owner = owner

    def like(self, user):
        net = SocialNetwork.SocialNetwork("")
        if net.is_online(user.name):
            self.likes.add(user.name)
            if self.owner != user:
                notification_message = f"{user.name} liked your post"
                self.owner.update(notification_message, True)
        return

    def comment(self, user, desc):
        net = SocialNetwork.SocialNetwork("")
        if net.is_online(user.name):
            self.comments.append((user, desc))
            if self.owner.name != user.name:
                notification_message = f"{user.name} commented on your post: {desc}"
                self.owner.update(notification_message, True)
        return

    def __post_as_string(self):
        pass

    def print(self):
        pass


class TextPost(Post):
    content = ""

    def __init__(self, owner,content):
        super().__init__(owner)
        self.content = content
        self.print()

    def print(self):
        print(self.__post_as_string())

    def __post_as_string(self):
        return f"{self.owner.name} published a post:\n{self.content}"

    def __str__(self):
        return self.__post_as_string()

class ImagePost(Post):
    image_url = ""

    def __init__(self, owner, image_url):
        super().__init__(owner)
        self.image_url = image_url
        self.print()
        msg = self.__post_as_string()
        owner.notify(msg, False)

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
        return f"{self.owner.name} posted a picture"
    def __str__(self):
        return self.__post_as_string()


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
        self.owner.notify(self.__post_as_string(), False)

    def discount(self, amount_of_discount, password):
        if self.owner.correct_password(password):
            self.price = self.price * (1-amount_of_discount/100)
            msg = f"Discount on {self.owner.name} product! the new price is: {self.price}"
            print(msg)
            self.owner.notify(msg,False)
        return self

    def sold(self, password):
        if self.owner.correct_password(password):
            self.is_sold = True
            print(f"{self.owner.name}'s product is sold \n")

        return

    def print(self):
        print(self.__post_as_string())
        # sold_text = "Sold! " if self.is_sold else "For sale!"
        # print(self.owner.name + " posted a product for sale:")
        # print(f"{sold_text} {self.text}, price: {self.price}, pickup from {self.location}")

    def __str__(self):
        return self.__post_as_string()

    def __post_as_string(self):
        sold_text = "Sold! " if self.is_sold else "For sale!"
        msg = f"{self.owner.name} posted a product for sale:\n"
        msg = msg + f"{sold_text} {self.text}, price: {self.price}, pickup from {self.location}"
        return msg