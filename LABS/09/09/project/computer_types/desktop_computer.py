from project.computer_types.computer import Computer
from math import  log2

class DesktopComputer(Computer):
    _max_ram = 128
    _processors: dict = {'AMD Ryzen 7 5700G': 500
                         ,'Intel Core i5-12600K': 600
                         ,'Apple M1 Max': 1800
                         }

    _price_per_two_gb_ram = 100


    def configure_computer(self,processor: str, ram: int):
        if processor not in self._processors.keys():
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if ram %2 != 0 or ram > self._max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        ram_price  = int(log2(ram))

        self.processor = processor
        self.ram = ram
        self.price = ram_price * 100 + self._processors[processor]
        return f"Created {self.__repr__()} for {self.price}$."

