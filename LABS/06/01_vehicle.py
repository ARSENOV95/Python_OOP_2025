from abc import ABC,abstractmethod

class Vehicle(ABC):
    ADDITIONAL_CONSUMPTION = 0.0

    def __init__(self,fuel_quantity: int,fuel_consumption:int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, kilometers):
        total_consumption = self.fuel_consumption + self.ADDITIONAL_CONSUMPTION
        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    @abstractmethod
    def refuel(self,liters):
        pass

class Car(Vehicle):
    ADDITIONAL_CONSUMPTION = 0.9

    def __init__(self,fuel_quantity,fuel_consumption):
        super().__init__(fuel_quantity,fuel_consumption)

    def drive(self,kilometers):
        return self.fuel_quantity

    def refuel(self,liters):
        self.fuel_quantity += liters
        return self.fuel_quantity

class Truck(Vehicle):
    ADDITIONAL_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)


    def drive(self, kilometers):
        return self.fuel_quantity

    def refuel(self,liters):
        refuel_amount = (liters * 95)/100
        self.fuel_quantity += refuel_amount
        return self.fuel_quantity


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)