from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INIT_VOLUME = 8

    def __init__(self, code):
        super().__init__(code, self.INIT_VOLUME)

    def zone_info(self):
        ship_list = self.get_ships()
        total_ships = len(ship_list)
        royal_ships = sum(1 for ship in ship_list if isinstance(ship,RoyalBattleship))
        ship_names = ', '.join([ship.name for ship in ship_list]) if ship_list else ''

        result = (f"@Pirate Zone Statistics@\n"
                  f"Code: {self.code}; Volume: {self.volume}\n"
                  f"Battleships currently in the Royal Zone: {total_ships}, "
                  f"{royal_ships} out of them are Royal Battleships.")

        return  result + f'\n#{ship_names}#' if ship_names else ''
