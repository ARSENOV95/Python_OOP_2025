from abc import abstractmethod
from socket import send_fds

from project.animals.animal import Animal
from project.food import Food
from project.food import Meat
from project.food import Vegetable
from project.food import Seed
from project.food import Fruit



class Mammal(Animal):
    def __init__(self,name,weight,living_region :str):
        super().__init__(name,weight,0)
        self.living_region = living_region

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self,food :Food):
        super().feed(food)

    @abstractmethod
    def __repr__(self):
        pass



class Mouse(Mammal):
    WEIGHT_PER_MEAL = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self,food :Food):
        is_vegetable_or_fruit = isinstance(food,Vegetable) or isinstance(food,Fruit)
        if is_vegetable_or_fruit:
            super().feed(food)
            return None
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


    def __repr__(self):
            return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Dog(Mammal):
    WEIGHT_PER_MEAL = 0.40
    def make_sound(self):
        return "Woof!"

    def feed(self,food :Food):
        is_meat =  isinstance(food, Meat)
        if is_meat:
            super().feed(food)
            return None
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
            return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Cat(Mammal):
    WEIGHT_PER_MEAL = 0.30
    def make_sound(self):
        return "Meow"

    def feed(self,food :Food):
        is_vegetable_or_meat = isinstance(food, Vegetable) or isinstance(food, Meat)
        if is_vegetable_or_meat:
            super().feed(food)
            return None
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


    def __repr__(self):
            return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"



class Tiger(Mammal):
    WEIGHT_PER_MEAL = 1.00
    def make_sound(self):
        return "ROAR!!!"

    def feed(self,food :Food):
        is_meat =  isinstance(food, Meat)
        if is_meat:
            super().feed(food)
            return None
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
            return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

