from abc import abstractmethod

from project.animals.animal import Animal
from project.food import Food
from project.food import Meat
from project.food import Vegetable
from project.food import Seed
from project.food import Fruit


class Bird(Animal):
    def __init__(self,name,weight,wing_size):
        super().__init__(name,weight,0)
        self.wing_size = wing_size

    @abstractmethod
    def make_sound(self):
        pass


    def feed(self, food: Food):
        super().feed(food)


    def __repr__(self):
        pass


class Owl(Bird):

    WEIGHT_PER_MEAL = 0.25
    def make_sound(self):
        return "Hoot Hoot"

    def feed(self,food :Food):
        is_meat = isinstance(food,Meat)
        if is_meat:
            super().feed(food)
            return None
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
            return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Hen(Bird):
    WEIGHT_PER_MEAL = 0.35
    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        super().feed(food)


    def __repr__(self):
            return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
