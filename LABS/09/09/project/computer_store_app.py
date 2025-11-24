from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    computer_types:dict[str,type[Computer]] = {'Desktop Computer': DesktopComputer
                                              ,'Laptop': Laptop}

    def __init__(self):
        self.warehouse: list[Laptop|DesktopComputer] = []
        self.profits: int = 0

    def build_computer(self,type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.computer_types.keys():
            raise ValueError("{ type computer } is not a valid type computer!")

        curr_computer = self.computer_types[type_computer](manufacturer,model)
        result = curr_computer.configure_computer(processor, ram)

        self.warehouse.append(curr_computer)

        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int) -> str:
        computer = next((c for c in self.warehouse
                         if c.price <= client_budget and \
                         c.processor == wanted_processor and \
                         c.ram >= wanted_ram), None)

        if not computer:
            f"Sorry, we don't have a computer for you."

        self.profits = client_budget - computer.price
        self.warehouse.remove(computer)
        return f"{computer.__repr__()} sold for {client_budget}$."


