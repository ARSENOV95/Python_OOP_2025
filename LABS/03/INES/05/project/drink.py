from project.product import Product


class Drink(Product):
    def __init__(self,name :str):
        super().__init__(name,10) #goues torugh the parent init but sets the quntity as 10

