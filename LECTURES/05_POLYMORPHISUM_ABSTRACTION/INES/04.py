from abc import  ABC,abstractmethod
from math import  pi


class Shape(ABC):
    @abstractmethod

    def calculate_area(self):
        return None

    @abstractmethod
    def calculate_perimeter(self):
        return None

class Circle(Shape):
    __pi = pi
    def __init__(self,radius):
        self.__radius = radius

    def calculate_area(self):
        return self.__pi *(self.__radius**2)

    def calculate_perimeter(self):
        return 2*(self.__pi * self.__radius)

class Rectangle(Shape):
    def __init__(self,height,width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2*(self.__width + self.__height)
