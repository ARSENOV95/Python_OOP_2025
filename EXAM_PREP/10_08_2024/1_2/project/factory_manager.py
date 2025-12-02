from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore

product_mapper = {"Chair":Chair
                  ,"HobbyHorse":HobbyHorse
                  }
store_mapper = {'FurnitureStore':FurnitureStore
                ,'ToyStore':ToyStore
                }


class FactoryManager:
    def __init__(self,name :str):
        self.name = name
        self.income:float = 0.0
        self.products:list[BaseProduct] = []
        self.stores:list[BaseStore] = []

    def produce_item(self,product_type: str, model: str, price: float):
        if product_type not in product_mapper.keys():
            raise Exception("Invalid product type!")

        product = product_mapper[product_type](model,price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self,store_type: str, name: str, location: str):
        if store_type not in store_mapper:
            raise Exception(f"{store_type} is an invalid type of store!")

        store = store_mapper[store_type](name,location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."


    def sell_products_to_store(self,store: BaseStore, *products: BaseProduct):
        if len(products) > store.capacity:
            return f"Store {store.name} has no capacity for this purchase."

        store_type = store.store_type

        matching = [product for product in products if product.sub_type[:-1] in store_type]
        if not matching:
            return 'Products do not match in type. Nothing sold.'


        for i in range(len(matching)):
            store.products.append(matching[i])
            store.capacity -= 1
            self.products.remove(matching[i])
            self.income += matching[i].price
        return f"Store {store.name} successfully purchased {len(matching)} items."


    def check_for_store(self,name):
        return next((store for store in self.stores if store.name == name),None)


    def unregister_store(self,store_name: str):
        store = self.check_for_store(store_name)

        if store is None:
            raise Exception("No such store!")

        if len(store.products) > 0:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store.name}, location: {store.location}."

    def discount_products(self,product_model: str):
        products_for_discount = [product for product in self.products if product.model == product_model]
        [product.discount() for product in products_for_discount]

        return f"Discount applied to {len(products_for_discount)} products with model: {product_model}"

    def request_store_stats(self,store_name: str):
        store = self.check_for_store(store_name)
        if store is None:
            return "There is no store registered under this name!"

        return store.store_stats()

    def statistics(self):
        total_price = sum(product.price for product in self.products)
        sorted_stores = sorted(self.stores,key = lambda s: s.name)
        sorted_products = sorted(self.products,key = lambda p: p.model)

        models:dict[str,int] = {}

        for product in sorted_products:
            if product.model not in models.keys():
                models[product.model] = 0
            models[product.model] += 1


        stats = (f"Factory: {self.name}\nIncome: {self.income:.2f}\n"
                 f"***Products Statistics***\n"
                 f"Unsold Products: {len(sorted_products)}. Total net price: {total_price:.2f}\n")


        stats += '\n'.join(f"{model}: {count}" for model,count in models.items()) if sorted_stores else ''
        stats += f"\n***Partner Stores: {len(sorted_stores)}***\n"

        stats += '\n'.join(store.name for store in sorted_stores) if sorted_stores else ''

        return stats