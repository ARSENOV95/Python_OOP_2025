from project.product import Product

class ProductRepository(Product):
    def __init__(self):
        super().__init__(self)
        self.products: list[Product] = []

    def add(self,product: Product):
        self.products.append(product)

    def find(self,product_name: str):
        is_in_list = next((p for p in self.products if p.name == product_name),None)
        if is_in_list:
            return  product_name
        return None

    def remove(self,product_name):
        is_in_list = next((p for p in self.products if p.name == product_name), None)
        if is_in_list:
            self.products.remove(product_name)

    def __repr__(self):
        return "\n".join(f'{p.name}: {p.quantity}' for p in self.products)