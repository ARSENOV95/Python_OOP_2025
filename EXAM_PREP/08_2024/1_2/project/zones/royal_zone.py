from project.battleships.pirate_battleship import PirateBattleship
from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    INIT_VOLUME = 10
    
    def __init__(self,code):
        super().__init__(code,self.INIT_VOLUME)

    def zone_info(self):
        ship_list = self.get_ships()
        total_ships = len(ship_list)
        pirate_ships = sum(1 for ship in ship_list if isinstance(ship,PirateBattleship))
        ship_names = ', '.join([ship.name for ship in ship_list]) if ship_list else ' '

        result = (f"@Royal Zone Statistics@\n"
                  f"Code: {self.code}; Volume: {self.volume}\n"
                  f"Battleships currently in the Royal Zone: {total_ships}, "
                  f"{pirate_ships} out of them are Pirate Battleships.")

        return result + f"\n#{ship_names}#" if ship_names else result