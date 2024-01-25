from classes.Review import Review
class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price
        self.reviews = []

    def buy(self, user):
        user.buy_item(self)

    def add_review(self, title, description, star_count):
        review = Review(title, description, star_count)
        self.reviews.append(review)
