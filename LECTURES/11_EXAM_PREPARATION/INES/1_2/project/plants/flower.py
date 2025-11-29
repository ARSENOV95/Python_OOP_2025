from project.plants.base_plant import BasePlant


class Flower(BasePlant):
    SEASONS = ["Spring","Summer","Fall","Winter"]
    def __init__(self,name,price,water_needed,blooming_season :str):
        super().__init__(name,price,water_needed)
        self.__blooming_season = blooming_season

    @property
    def blooming_season(self):
        return

    @blooming_season.setter
    def blooming_season(self, value :str):
        if value not in self.SEASONS:
            raise ValueError("Blooming season must be a valid one!")
        self.__blooming_season = value

    def plant_details(self):
        return f"Flower: {self.name}, Price: {self.price:.2f}, Watering: {self.water_needed}ml, Blooming Season: {self.__blooming_season}"
