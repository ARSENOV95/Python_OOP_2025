from project.battleships.base_battleship import BaseBattleship


class PirateBattleship(BaseBattleship):
    INIT_AMMUNITION = 80
    AMMO_PER_ATTACK = 10

    def __init__(self,name,health,hit_strength):
        super().__init__(name,health,hit_strength,self.INIT_AMMUNITION)

    def attack(self):
        self.ammunition -= self.AMMO_PER_ATTACK
        if self.ammunition < 0:
            self.ammunition = 0

