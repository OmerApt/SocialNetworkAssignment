class PostsFactory:
    def create_text_post(self):
        pass
    def create_image_post(self):
        return
    def create_sale_post(self):
        return
class Post:
    likes=0
    comments={}

    def like(self,user):
        return
    def comment(self,user,desc):
        return


class TextPost(Post):
    x = 4
class ImagePost(Post):
    def display(self):
        return

class SalePost(Post):
    def discount(self, amountdis, password):
        return

    def sold(self, password):
        return