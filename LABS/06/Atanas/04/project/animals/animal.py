from abc import ABC,abstractmethod
from project.food import Food


class Animal(ABC):
    def __init__(self,name :str,weight :float,food_eaten: int = 0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @property  # toi make the whole logic work we set abstact properties  which should be in all sublasses
    @abstractmethod
    def allowed_food(self) -> list[Food]:
        pass

    @property
    @abstractmethod
    def weight_increment(self)->float:
        pass

    @staticmethod #deocrators can stack!
    @abstractmethod
    def make_sound():
        pass
    
    def feed(self,food :Food) -> None | str:
        if type(food) not in self.allowed_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += (self.weight_increment * food.quantity)
        self.food_eaten += food.quantity
        return None

class Bird(Animal,ABC):
    def __init__(self,name,weight,wing_size :float):
        super().__init__(name,weight)
        self.wing_size = wing_size

    def __repr__(self) ->str:
            return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal,ABC):
    def __init__(self,name,weight,living_region :str):
        super().__init__(name,weight)
        self.living_region = living_region

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"