from urllib.request import parse_http_list

from clients.base_client import BaseClient
from clients.business_client import BusinessClient
from clients.regular_client import RegularClient
from plants.base_plant import BasePlant
from plants.leaf_plant import LeafPlant
from plants.flower import Flower

mapper = {"Flower": Flower,
               "LeafPlant": LeafPlant
               }
client_mapper = {"RegularClient": RegularClient,
                "BusinessClient": BusinessClient
                }

class FlowerShopManager:
    orders = 0

    def __init__(self):
        self.income:float = 0.0
        self.plants:list[BasePlant] = []
        self.clients:list[BaseClient] = []

    def add_plant(self,plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str)-> str:

        if plant_type not in mapper:
            raise ValueError("Unknown plant type!")

        plant = mapper[plant_type](plant_name,plant_price,plant_water_needed,plant_extra_data)
        self.plants.append(plant)

        return f"{plant_name} is added to the shop as {plant_type}."


    def filter_clients(self,phone_number):
        return next((c for c in self.clients if c.phone_number == phone_number), None)

    def filter_plants(self,name):
        return [p for p in self.plants if p.name == name]



    def add_client(self,client_type: str, client_name: str, client_phone_number: str)-> str:
        if client_type not in client_mapper:
            raise ValueError("Unknown client type!")

        client = self.filter_clients(client_phone_number)
        if client is not None:
            raise ValueError("This phone number has been used!")

        client = client_mapper[client_type](client_name,client_phone_number)
        self.clients.append(client)

        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self,client_phone_number: str, plant_name: str, plant_quantity: int)->str|None:
        client = self.filter_clients(client_phone_number)

        if client is None:
            raise ValueError("Client not found!")

        plants = self.filter_plants(plant_name)

        if plants is None:
            raise ValueError("Plants not found!")

        if len(plants) <= plant_quantity:
            return "Not enough plant quantity."

        order_amount  =0

        for i in range(plant_quantity):
            curr_plant = plants[i]
            self.plants.remove(curr_plant)
            discount = client.discount/100
            order_amount +=  curr_plant.price - (curr_plant.price * discount)

        self.income += order_amount

        client.update_total_orders()
        client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"

    def remove_plant(self,plant_name: str):
        plants = self.filter_plants(plant_name)

        if plants is None:
            return "No such plant"

        self.plants.remove(plants[0])
        plant_to_remove = plants[0].plant_details()

        return f"Removed {plant_to_remove}"


    def remove_clients(self):
        no_orders_clients = [c for c in self.clients if c.total_orders != 0]

        for i in range(len(no_orders_clients)):
            self.clients.remove(no_orders_clients[i])
        return f"{len(no_orders_clients)}  client/s removed."


    def shop_report(self):
        result = []

        flowers_count = {}
        for flower in self.plants:
            flowers_count[flower.name] = len(self.filter_plants(flower.name))

        sorted_flowers_count = sorted(flowers_count.items(),key = lambda kvp: (-kvp[1],kvp[0]))
        sorted_clients = sorted(self.clients,key = lambda  client: (-client.total_orders,client.phone_number))


        all_orders = sum([client.total_orders for client in self.clients])
        result.append(f"~Flower Shop Report~\nIncome: {self.income:.2f}\nCount of orders: {all_orders}\n~~Unsold plants: {len(self.plants)}~~")
        for plant_name,plant_count in sorted_flowers_count:
            result.append(f"{plant_name}: {plant_count}")

        result.append(f"~~Clients number: {len(self.clients)}~~")
        for client in sorted_clients:
            result.append(client.client_details())

        return "\n".join(result)