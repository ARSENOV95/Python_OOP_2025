from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse: list[Laptop|DesktopComputer] = []
        self.profits: int = 0

    def build_computer(self,type_computer: str, manufacturer: str, model: str, processor: str, ram: int):

        if type_computer not in ('Desktop Computer','Laptop'):
            raise ValueError(f"{type_computer} is not a valid type computer!")

        if type_computer ==  'Desktop Computer':
            computer = DesktopComputer(manufacturer,model)
        else:
            computer = Laptop(manufacturer, model)

        if computer.configure_computer(processor,ram):
            self.warehouse.append(computer)

        return computer.configure_computer(processor,ram)

    def sell_computer(self,client_budget: int, wanted_processor: str, wanted_ram: int):

        for computer in self.warehouse:
            if computer.price <= client_budget and computer.processor == wanted_processor and computer.ram >= wanted_ram:
                self.profits = client_budget - computer.price
                return f"{computer.__repr__()} sold for {client_budget}$."

        return f"Sorry, we don't have a computer for you."





