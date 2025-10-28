class Laptop:
    def __init__(self, model):
        self.model = model
 my_laptop = Laptop("Swift")
 my_laptop.ram = 8
 Laptop.brand = "Dell"
 del my_laptop.model