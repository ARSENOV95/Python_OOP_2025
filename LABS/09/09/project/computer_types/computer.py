from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self,manufacturer: str,model: str):
        self.__manufacturer = manufacturer
        self.__model = model
        self.processor: str | None = None
        self.ram: str | None = None
        self.price:int = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model (self):
        return self.__model
    
    @model .setter
    def model (self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @abstractmethod
    def configure_computer(self,processor: str, ram :int):
        pass

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"



