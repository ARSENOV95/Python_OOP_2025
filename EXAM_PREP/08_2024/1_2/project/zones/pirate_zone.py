from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INIT_VOLUME = 8

    def __init__(self, code):
        super().__init__(code, self.INIT_VOLUME)

    def zone_info(self):
        info = ['@Pirate Zone Statistics@', f'Code: {self.code}; Volume: {self.volume}']

        royal_ships = [ship for ship in self.ships if isinstance(ship,RoyalBattleship)]

        info.append(
            f'Battleships currently in the Pirate Zone: {len(self.ships)},{len(royal_ships)} out of them are Royal Battleships')
        info.append(f"#{', '.join(self.get_ships())}#")

        return '\n'.join(info)