from abc import ABC, abstractmethod

import matplotlib.pyplot as plt

from Users import User
from builtins import list


class PostsFactory(ABC):
    @abstractmethod
    def create_post(self, *args):
        pass

    def make_post(self, *args):
        return self.create_post(*args)


class TextPostFactory(PostsFactory):

    def create_post(self, *args):
        usr = args[0]
        text = args[1]
        return TextPost(owner=usr, content=text)


class ImagePostFactory(PostsFactory):
    def create_post(self, *args):
        return ImagePost(owner=args[0], image_url=args[0])


class SalePostFactory(PostsFactory):
    def create_post(self, *args):
        owner = args[0]
        text = args[1]
        price = args[2]
        location = args[3]
        return SalePost(owner, text, price, location)


class Post:
    likes = set()
    comments = list()
    owner = ''

    def __init__(self, owner):
        self.owner = owner

    def notify(self):
        return

    def like(self, user):
        self.likes.add(user)
        if self.owner != user:
            self.owner.notify()
        return

    def comment(self, user, desc):
        self.comments.append((user, desc))
        return

    def print(self):
        pass


class TextPost(Post):
    content = ""

    def __init__(self, content, owner):
        super().__init__(owner)
        self.content = content

    def print(self):
        print(self.owner + " published a post:\n" + self.content)


class ImagePost(Post):
    image_url = ""

    def __init__(self, owner, image_url):
        super().__init__(owner)
        self.image_url = image_url

    def display(self):
        try:
            plt.imshow(self.image_url)
            print("Shows picture")
        except FileNotFoundError:
            print("No image found")
        return

    def print(self):
        print(self.owner + " posted a picture")


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

    def discount(self, amountOfDiscount, password):
        if self.owner.correct_password(password):
            self.price = self.price / amountOfDiscount
        return self

    def sold(self, password):
        if self.owner.correct_password(password):
            self.is_sold = True
            print(f"{self.owner}'s product is sold \n")

        return

    def print(self):
        soldtext = "Sold! " if self.is_sold else "For sale!"
        print(self.owner.name + " posted a product for sale:\n")
        print(f"{soldtext} {self.text}, price: {self.price}, pickup from {self.location}\n")
