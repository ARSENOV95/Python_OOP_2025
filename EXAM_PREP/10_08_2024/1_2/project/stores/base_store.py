from abc import ABC,abstractmethod

from project.products.base_product import BaseProduct


class BaseStore(ABC):
    VAT = 10

    def __init__(self,name :str,location :str,capacity :int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: list[BaseProduct] = []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value :str):
        if not value.strip:
            raise ValueError("Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location
    
    @location.setter
    def location(self, value :str):
        if len(value.strip()) != 3 or ' ' in value.strip():
            raise ValueError("Store location must be 3 chars long!")
        self.__location = value

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value :int):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value


    def get_estimated_profit(self):
        profit = (sum(product.price for product in self.products)) * (self.VAT/100)
        return f"Estimated future profit for {len(self.products)} products is {profit:.2f}"

    @property
    def store_type(self):
        return self.__class__.__name__

    @abstractmethod
    def store_stats(self):
        pass
