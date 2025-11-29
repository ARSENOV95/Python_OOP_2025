from numpy.f2py.auxfuncs import istrue

from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone

zones_types: dict[str:BaseZone] = {"RoyalZone":RoyalZone,"PirateZone":PirateZone}
ship_types: dict[str:BaseBattleship] = {'RoyalBattleship':RoyalBattleship,
                                        'PirateBattleship':PirateBattleship
                                        }

class BattleManager:
    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list[BaseBattleship] = []



    #check for zone with existing code in the zones list
    def zone_with_code_exists(self,code):
        return next((z for z in self.zones if z.code == code),None)


    def add_zone(self,zone_type: str, zone_code: str):

        if zone_type not in zones_types:
            raise Exception("Invalid zone type!")

        zone = self.zone_with_code_exists(zone_code)

        if zone is not None:
            raise Exception("Zone already exists!")

        zone = zones_types[zone_type](zone_code)
        self.zones.append(zone)
        return f"A zone of type {zone_type} was successfully added."


    def add_battleship(self,ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in ship_types:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        ship = ship_types[ship_type](name,health,hit_strength)
        self.ships.append(ship)
        return f"A new {ship_type} was successfully added."


    def add_ship_to_zone(self,zone: BaseZone, ship: BaseBattleship):
        if zone.volume == 0:
            return f"Zone {zone.code} does not allow more participants!"

        if not ship.health > 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        ship_type = ship.__name__
        print(ship_type)


    def remove_battleship(self,ship_name: str):
        pass

    def start_battle(self,zone: BaseZone):
        pass

    def get_statistics(self):
        pass