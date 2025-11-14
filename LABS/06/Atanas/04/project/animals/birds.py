from project.animals.animal import Bird
from project.food import Food,Meat,Vegetable,Fruit,Seed



class Owl(Bird):
    @property
    def allowed_food(self):
        return [Meat]

    @property
    def weight_increment(self) -> float:
        return 0.25

    @staticmethod
    def make_sound() ->str:
        return "Hoot Hoot"

    #SINCE ITS NOT ABSTRACT THE FEED code will not be included, whne called, it will look trough the parent scpe for the logic and execute it based on the proeprites

class Hen(Bird):
    @property
    def allowed_food(self):
        return [Meat,Vegetable,Fruit,Seed]

    @property
    def weight_increment(self) -> float:
        return 0.35


    @staticmethod
    def make_sound() -> str:
        return "Cluck"

