from project.computer_types.computer import Computer
from math import  log2

class DesktopComputer(Computer):
    max_ram = 128
    processors: dict = {'AMD Ryzen 7 5700G': 500
                         ,'Intel Core i5-12600K': 600
                         ,'Apple M1 Max': 1800
                         }



    def configure_computer(self,processor: str, ram: int):
        valid_ram = [2 ** i for i in range(1, int(log2(self.max_ram))+1)]
        if processor not in self.processors.keys():
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if ram not in valid_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        ram_price  = int(log2(ram)) * 100

        self.processor = processor
        self.ram = ram
        self.price = ram_price + self.processors[processor]
        return f"Created {self.__repr__()} for {self.price}$."

