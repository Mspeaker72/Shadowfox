class Bread:
    def __init__(self):
        self.products = []

    def __add__(self, product):
        if product not in self.products:
            self.products.append(product)

    def get_products(self):
        return self.products




