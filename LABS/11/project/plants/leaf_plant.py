from plants.base_plant import BasePlant


class LeafPlant(BasePlant):
    def __init__(self,name,price,water_needed,size :str):
        super().__init__(name,price,water_needed)
        self.__size = size

    @property
    def size(self):
        return

    @size.setter
    def size(self, value :str):
        valid_sizes = ("S","M","L")
        if value not in valid_sizes:
            raise ValueError("Size must be a valid one!")

        self.__size = value

    def plant_details(self):
        return f"Leaf Plant: {self.name}, Price: {self.price}, Watering: {self.water_needed}ml, Size: {self.__size}"