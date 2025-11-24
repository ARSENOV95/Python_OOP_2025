from project.computer_types.computer import Computer
from math import  log2

class Laptop(Computer):

    max_ram = 64
    processors: dict = {'AMD Ryzen 9 5950X': 900
                         ,'Intel Core i9-11900H': 1050
                         ,'Apple M1 Pro': 1200
                         }

    price_per_two_gb_ram = 100


    def configure_computer(self, processor: str, ram: int):
        valid_ram = [2 ** i for i in range(1, int(log2(self.max_ram)) + 1)]
        if processor not in self.processors.keys():
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        if ram not in valid_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        ram_price  = int(log2(ram)) * 100


        self.processor = processor
        self.ram = ram
        self.price = ram_price  + self.processors[processor]
        return f"Created {self.__repr__()} for {self.price}$."
