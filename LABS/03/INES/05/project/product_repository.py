from project.product import Product

class ProductRepository:
    def __init__(self):
        self.products: list[Product] = []

    def add(self,product: Product):
        self.products.append(product)

    def find(self,product_name :str):
        product = [p for p in self.products if p.name == product_name]
        return product

    def remove(self,product_name :str):
        product = next((p for p in self.products if p.name == product_name),None)
    #product = [p for p in self.products if p.name == product_name][0 ] - it is the same as next it retruns a list and takes its first value
        if product:
            self.products.remove(product)

    def __repr__(self) -> str:
        return "\n".join(f'{p.name}: {p.quantity}' for p in self.products)
