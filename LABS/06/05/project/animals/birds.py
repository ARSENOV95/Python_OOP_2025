from project.animals.animal import Bird
from project.food import Food
from project.food import Meat
from project.food import Vegetable
from project.food import Seed
from project.food import Fruit



class Owl(Bird):
    WEIGHT_PER_MEAL = 0.25

    @staticmethod
    def make_sound() ->str:
        return "Hoot Hoot"

    def feed(self,food :Food) ->str | None:
        is_meat = isinstance(food,Meat)
        if is_meat:
            self.food_eaten += food.quantity
            self.weight += (self.WEIGHT_PER_MEAL * food.quantity)
            return None
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self) ->str:
            return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Hen(Bird):
    WEIGHT_PER_MEAL = 0.35

    @staticmethod
    def make_sound()->str:
        return "Cluck"

    def feed(self, food: Food) ->str | None:
        self.food_eaten += food.quantity
        self.weight += (self.WEIGHT_PER_MEAL * food.quantity)


    def __repr__(self) -> str:
            return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
