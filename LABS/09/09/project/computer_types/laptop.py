from project.computer_types.computer import Computer
from math import  log2

class Laptop(Computer):

    _max_ram = 64
    _processors: dict = {'AMD Ryzen 9 5950X': 900
                         ,'Intel Core i9-11900H': 1050
                         ,'Apple M1 Pro': 1200
                         }

    _price_per_two_gb_ram = 100


    def configure_computer(self, processor: str, ram: int):
        if processor not in self._processors.keys():
            raise ValueError(f"{ processor } is not compatible with laptop {self.manufacturer} {self.model}!")

        if ram % 2 != 0 or ram > self._max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        ram_price  = int(log2(ram))


        self.processor = processor
        self.ram = ram
        self.price = ram_price * 100 + self._processors[processor]
        return f"Created {self.__repr__()} for {self.price}$."
