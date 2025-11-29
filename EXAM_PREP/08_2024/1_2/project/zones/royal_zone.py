from project.battleships.pirate_battleship import PirateBattleship
from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    INIT_VOLUME = 10
    
    def __init__(self,code):
        super().__init__(code,self.INIT_VOLUME)

    def zone_info(self):
        info = ['@Royal Zone Statistics@',f'Code: {self.code}; Volume: {self.volume}']

        pirate_ships = [ship for ship in self.ships if isinstance(ship,PirateBattleship)]

        info.append(f'Battleships currently in the Royal Zone: {len(self.ships)},{len(pirate_ships)} out of them are Pirate Battleships.')
        info.append(f"#{', '.join(self.get_ships())}#")

        return '\n'.join(info)