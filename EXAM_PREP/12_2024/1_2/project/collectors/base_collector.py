from abc import ABC,abstractmethod
import re

from project.artifacts.base_artifact import BaseArtifact


class BaseCollector(ABC):
    def __init__(self,name: str,available_money: float,available_space: int):
        self.__name = name
        self.__available_money = available_money
        self.__available_space = available_space
        self.purchased_artifacts: list[BaseArtifact] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not re.match(r'^[A-Za-z0-9][A-Za-z0-9\s]*[A-Za-z0-9]$',value):
            raise ValueError("Collector name must contain letters, numbers, and optional white spaces between them!")
        self.__name = value
        
    @property
    def available_money(self):
        return self.__available_money
    
    @available_money.setter
    def available_money(self, value :float):
        if value < 0.0:
            raise ValueError("A collector cannot have a negative amount of money!")
        self.__available_money = value

    @property
    def available_space(self):
        return  self.__available_space

    @available_space.setter
    def available_space(self, value :int):
        if value < 0:
            raise ValueError("A collector cannot have a negative space available for exhibitions!")
        self.__available_space = value

    @abstractmethod
    def increase_money(self):
        pass

    def can_purchase(self,artifact_price: float, artifact_space_required: int):
        return self.available_money >= artifact_price and self.available_space > artifact_space_required

    def __str__(self):
        artefacts = ', '.join(sorted([a.name for a in self.purchased_artifacts],reverse= True)) if self.purchased_artifacts else 'None'
        return f"Collector name: {self.name}; Money available: {self.available_money:.2f}; Space available: {self.available_space}; Artifacts: {artefacts}"

