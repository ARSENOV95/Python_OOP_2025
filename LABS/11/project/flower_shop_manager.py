from clients.base_client import BaseClient
from clients.business_client import BusinessClient
from clients.regular_client import RegularClient
from plants.base_plant import BasePlant
from plants.leaf_plant import LeafPlant
from plants.flower import Flower

class FlowerShopManager:
    orders = 0

    def __init__(self):
        self.income:float = 0.0
        self.plants:list[BasePlant] = []
        self.clients:list[BaseClient] = []

    def add_plant(self,plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str)-> str:
        plant_types = {"Flower": Flower,
                       "LeafPlant": LeafPlant
                       }

        if plant_type not in plant_types:
            raise ValueError("Unknown plant type!")

        plant = plant_types[plant_type](plant_name,plant_price,plant_water_needed,plant_extra_data)
        self.plants.append(plant)

        return f"{plant_name} is added to the shop as {plant_type}."


    def add_client(self,client_type: str, client_name: str, client_phone_number: str)-> str:
        client_types = {"RegularClient":RegularClient,
                        "BusinessClient":BusinessClient
                        }

        if client_type not in client_types:
            raise ValueError("Unknown client type!")

        client = next((c for c in self.clients if c.phone_number == client_phone_number and c.name != client_name),None)

        if client:
            raise ValueError("This phone number has been used!")

        client = client_types[client_type](client_name,client_phone_number)
        self.clients.append(client)

        return f"{client_name} is successfully added as a {client_type}."


    def sell_plants(self,client_phone_number: str, plant_name: str, plant_quantity: int)->str|None:
        client = next((c for c in self.clients if c.phone_number == client_phone_number),None)

        if not client:
            raise ValueError("Client not found!")

        plant = next((p for p in self.plants if p.name == plant_name),None)

        num_plants = len([p.name for p in self.plants if p.name == plant_name])

        if num_plants < plant_quantity:
            return "Not enough plant quantity."



        for _ in range(plant_quantity):
            curr_plant = next(p for p in self.plants if p.name == plant_name)
            self.plants.remove(curr_plant)


        order_total = (plant.price * plant_quantity) - ((plant.price * plant_quantity) * client.discount)

        self.income += order_total


        client.update_total_orders()
        self.orders += 1

        client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_total:.2f}"


    def remove_plant(self,plant_name: str):
        plant = next((p for p in self.plants if p.name == plant_name),None)

        if not plant:
            return "No such plant"
        self.plants.remove(plant)

        return f"Removed {plant.plant_details()}"


    def remove_clients(self):
        count_removed = 0

        removed = [c for c in self.clients if c.total_orders != 0]
        count_removed = len(self.clients) - len(removed)

        self.clients = removed
        return f"{count_removed} client/s removed."


    @staticmethod
    def unsold_plants(obj :list[BasePlant])-> list:
        unsold = {}

        for o in obj:
            if o.name not in unsold.keys():
                unsold[o.name] = 0
            unsold[o.name] += 1

        sorted_unsold_plants = sorted(unsold.items(),key = lambda x: (-x[1],x[0]))
        return sorted_unsold_plants

    @staticmethod
    def unsold_clients(obj :list[BaseClient])-> list:
        sorted_obj: list[BaseClient]= []
        sorted_obj = sorted(obj,key = lambda o: (-o.total_orders,o.phone_number))
        return sorted_obj




    def shop_report(self):
        unsold_plans = self.unsold_plants(self.plants)
        unsold_clients = self.unsold_clients(self.clients)

        report = f"~Flower Shop Report~\nIncome: {self.income:.2f}\n'Count of orders: {self.orders}\n"
        report += f"~~Unsold plants: {len(self.plants)}~~\n"

        for plant in unsold_plans:
            report += f"{plant[0]}: {plant[1]}\n"

        report += f"~~Unsold plants: {len(self.clients)}~~\n"

        for client in unsold_clients:
            report += f"{client.client_details()}\n"

        return report