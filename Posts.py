import matplotlib.pyplot as plt
from Users import User
from builtins import list
from enum import Enum
from SocialNetwork import SocialNetwork


class Post_type(Enum):
    text = "Text"
    image = "Image"
    sale = "Sale"


class PostsFactory:
    def create_post(self, post_type, *args):
        if post_type == Post_type.text:
            return TextPost(*args)
        elif post_type == Post_type.image:
            return ImagePost(*args)
        elif post_type == Post_type.sale:
            return SalePost(*args)


class Post:
    likes = set()
    comments = list()
    owner = ''
    _net = SocialNetwork("")

    def __init__(self, owner):
        self.owner = owner

    def like(self, user):
        if self._net.is_online(user):
            self.likes.add(user)
            if self.owner != user:
                notification_message = f"{user.name} liked your post"
                self.owner.update(notification_message)
        return

    def comment(self, user, desc):
        if self._net.is_online(user):
            self.comments.append((user, desc))
            if self.owner != user:
                notification_message= f" commented on your post: {desc}"
                self.owner.update(notification_message)
        return

    def __post_as_string(self):
        pass

    def print(self):
        pass


class TextPost(Post):
    content = ""

    def __init__(self, content, owner):
        super().__init__(owner)
        self.content = content

    def print(self):
        print(self.__post_as_string())

    def __post_as_string(self):
        return self.owner + " published a post:\n" + self.content


class ImagePost(Post):
    image_url = ""

    def __init__(self, owner, image_url):
        super().__init__(owner)
        self.image_url = image_url
        msg = ""
        owner.notify(msg)

    def display(self):
        try:
            plt.imshow(self.image_url)
            print("Shows picture")
        except FileNotFoundError:
            print("No image found")
        return
    def print(self):
        print(self.__post_as_string())

    def __post_as_string(self):
        return self.owner + " posted a picture"


class SalePost(Post):
    text = ""
    price = 0.0
    location = ""
    is_sold = False
    amountOfDiscount = 0.0

    def __init__(self, owner, text, price, location):
        super().__init__(owner)
        self.text = text
        self.price = float(price)
        self.location = location
        self.is_sold = False
        self.owner.notify(self.__post_as_string())

    def discount(self, amount_of_discount, password):
        if self.owner.correct_password(password):
            self.price = self.price / amount_of_discount
            msg = f"Discount on {self.owner.name} product! the new price is: {self.price}"
            print(msg)
            self.owner.notify(msg)
        return self

    def sold(self, password):
        if self.owner.correct_password(password):
            self.is_sold = True
            print(f"{self.owner}'s product is sold \n")

        return

    def print(self):
        sold_text = "Sold! " if self.is_sold else "For sale!"
        print(self.owner.name + " posted a product for sale:")
        print(f"{sold_text} {self.text}, price: {self.price}, pickup from {self.location}")

    def __post_as_string(self):
        sold_text = "Sold! " if self.is_sold else "For sale!"
        msg = f"{self.owner.name} posted a product for sale:\n"
        msg = msg + f"{sold_text} {self.text}, price: {self.price}, pickup from {self.location}"
