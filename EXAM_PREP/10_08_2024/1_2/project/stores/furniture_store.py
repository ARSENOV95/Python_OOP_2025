from project.products.base_product import BaseProduct
from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    INITIAL_CAPACITY = 50

    def __init__(self,name: str,location: str):
        super().__init__(name,location,self.INITIAL_CAPACITY)

    def store_stats(self):
        profit = self.get_estimated_profit()

        sorted_products:list[BaseProduct] = sorted(self.products,key = lambda p: p.model)
        models:dict[str,list[float]] = {}

        for product in sorted_products:
            if product.model not in models.keys():
                models[product.model] = []
            models[product.model].append(product.price)

        stats = (f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
                 f"{profit}\n"
                 f"**Furniture for sale:\n")

        stats += '\n'.join(f'{model}: {len(prices)}pcs, '
                          f'average price: {sum(prices)/len(prices):.2f}'for model,prices in models.items()) if self.products else ''

        return stats
