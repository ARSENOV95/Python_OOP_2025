from abc import ABC,abstractmethod
import re

from project.artifacts.base_artifact import BaseArtifact


class BaseCollector(ABC):

    def __init__(self,name :str,available_money: float,available_space: int):
        self.__name = name
        self.__available_money = available_money
        self.__available_space = available_space
        self.purchased_artifacts: list[BaseArtifact] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        pattern = r'^[A-Za-z0-9]+[A-Za-z0-9\s]+[A-Za-z0-9]$'
        match = re.match(pattern,value)

        if not match:
            raise ValueError("Collector name must contain letters, numbers, and optional white spaces between them!")
        self.__name = value


    @property
    def available_money(self):
        return

    @available_money.setter
    def available_money(self, value):
        if  value <= 0:
            raise ValueError("A collector cannot have a negative amount of money!")
        self.__available_money = value

    @property
    def available_space(self):
        return self.__available_space
    
    @available_space.setter
    def available_space(self, value):
        if value <=0:
            raise ValueError("A collector cannot have a negative space available for exhibitions!")
        self.__available_space = value

    def increase_money(self,amaount):
        pass

