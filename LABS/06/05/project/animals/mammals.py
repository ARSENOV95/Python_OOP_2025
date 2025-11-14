from project.animals.animal import Mammal
from project.food import Food
from project.food import Meat
from project.food import Vegetable
from project.food import Seed
from project.food import Fruit





class Mouse(Mammal):
    WEIGHT_PER_MEAL = 0.10

    @staticmethod
    def make_sound()->str:
        return "Squeak"

    def feed(self,food :Food)-> None | str:
        if  isinstance(food,Vegetable) or isinstance(food,Fruit):
            self.food_eaten += food.quantity
            self.weight += (self.WEIGHT_PER_MEAL * food.quantity)
            return None
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


    def __repr__(self)->str:
            return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Dog(Mammal):
    WEIGHT_PER_MEAL = 0.40

    @staticmethod
    def make_sound()->str:
        return "Woof!"

    def feed(self,food :Food) -> None | str:
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += (self.WEIGHT_PER_MEAL * food.quantity)
            return None
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
            return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Cat(Mammal):
    WEIGHT_PER_MEAL = 0.30

    @staticmethod
    def make_sound() -> str:
        return "Meow"

    def feed(self,food :Food) -> None | str:
        if isinstance(food, Vegetable) or isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += (self.WEIGHT_PER_MEAL * food.quantity)
            return None
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


    def __repr__(self) -> str:
            return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"



class Tiger(Mammal):
    WEIGHT_PER_MEAL = 1

    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"

    def feed(self,food :Food) -> None | str:
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += (self.WEIGHT_PER_MEAL * food.quantity)
            return None
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self) -> str:
            return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

