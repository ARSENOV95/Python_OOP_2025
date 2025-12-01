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


    #Helper methods
    #check for zone with existing code in the zone list
    def zone_with_code_exists(self,code):
        return next((z for z in self.zones if z.code == code),None)

    #check for a ship with a name in the manager's collection
    def ship_with_name_exists(self,name):
        return next((s for s in self.ships if s.name == name),None)

    @staticmethod
    def check_ship_type(ship_clss: BaseBattleship):
        ship_type = ship_clss.__class__.__name__
        return ship_type[:ship_type.find('Battleship')]

    @staticmethod
    def check_zone_type(zone_clss: BaseZone):
        zone_type = zone_clss.__class__.__name__
        return  zone_type[:zone_type.find('Zone')]

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
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if not ship.health > 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        curr_ship = self.check_ship_type(ship)
        curr_zone = self.check_zone_type(zone)

        if curr_ship == curr_zone:
            ship.is_attacking = True

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1
        return  f"Ship {ship.name} successfully participated in zone {zone.code}."


    def remove_battleship(self,ship_name: str):
        ship = self.ship_with_name_exists(ship_name)

        if ship is None:
            return "No ship with this name!"

        if not ship.is_available:
            return  "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)
        return f"Successfully removed ship {ship.name}."

    def start_battle(self,zone: BaseZone):
        zone_type = self.check_zone_type(zone)
        # if the ship type is ! then the zone type and is not an attacker

        attacked_ships = [ship for ship in zone.ships
                                 if self.check_ship_type(ship) != zone_type
                                    and ship.is_attacking is False]
        #TODO_CHECK_LOGIC

        attacker_ships = [ship for ship in zone.ships
                                 if self.check_ship_type(ship) == zone_type
                                    and ship.is_attacking is True]


        if not (attacked_ships and attacker_ships):
            return "Not enough participants. The battle is canceled."

        attacked_ships:list[BaseBattleship] = sorted(attacked_ships,key=lambda s: -s.health)
        attacker_ships:list[BaseBattleship] = sorted(attacker_ships,key=lambda s: -s.hit_strength)

        #print(', '.join([s.name for s in attacked_ships]))
        #print(', '.join([s.name for s in attacker_ships]))

        attacker = attacker_ships[0]
        attacked = attacked_ships[0]


        attacker.attack()
        attacked.take_damage(attacker)

        if attacked.health <= 0:
            zone.ships.remove(attacked)
            self.ships.remove(attacked)
            #print(len(zone.ships))
            #print(len(self.ships))
            return f"{attacked.name} lost the battle and was sunk."

        if attacker.ammunition <= 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."
        #print(attacker.ammunition)
        #print(attacked.health)


    def get_statistics(self):
        available_ships= [s for s in self.ships if s.is_available]

        available_ships_str = ', '.join(ship.name for ship in available_ships) if available_ships else ''
        zones_info = '\n'.join(zone.zone_info() for zone in sorted(self.zones, key=lambda z: z.code))

        result = f"Available Battleships: {len(available_ships)}\n"
        result += f"#{available_ships_str}#\n" if available_ships else ''
        result += (f"***Zones Statistics:***\n"
                   f"Total Zones: {len(self.zones)}"
                   f"\n{zones_info}")
        return result.strip()
