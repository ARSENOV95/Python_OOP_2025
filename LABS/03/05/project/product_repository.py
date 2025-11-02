from project.product import Product

class ProductRepository:
    def __init__(self):
        self.products:list[Product] = []

    def add(self,product: Product) -> None:
        self.products.append(product)
        return  None

    def find(self,product_name: str) -> str | None:
        in_list = next((p for p in self.products if p.name == product_name),None)
        if in_list:
            return  in_list
        return None

    def remove(self,product_name):
        in_list = next((p for p in self.products if p.name == product_name), None)
        if in_list:
            self.products.remove(in_list)

    def __repr__(self):
        return "\n".join(f'{p.name}: {p.quantity}' for p in self.products)