class FreeUser:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.total_spent = 0

    def say_name(self):
        return f"My name is {self.first_name} {self.last_name}"

    def buy_item(self, product):
        self.total_spent += product.price

