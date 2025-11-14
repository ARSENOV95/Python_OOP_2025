from abc import ABC,abstractmethod
from project.food import Food

class Animal(ABC):
    def __init__(self,name :str,weight :float,food_eaten = 0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @staticmethod
    @abstractmethod
    def make_sound()->str:
        pass

    @abstractmethod
    def feed(self, food: Food):
        pass

    @abstractmethod
    def  __repr__(self)->str:
        pass


class Mammal(Animal,ABC):
    def __init__(self,name,weight,living_region :str):
        super().__init__(name,weight,0)
        self.living_region = living_region




class Bird(Animal,ABC):
    def __init__(self,name,weight,wing_size):
        super().__init__(name,weight,0)
        self.wing_size = wing_size

