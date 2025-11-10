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

    @property
    def radius(self):
        return self.__radius

    def calculate_area(self):
        return self.__pi *(self.__radius**2)

    def calculate_perimeter(self):
        return 2*(self.__pi * self.__radius)

class Rectangle(Shape):
    def __init__(self,height,width):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2*(self.__width + self.__height)


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())


rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())