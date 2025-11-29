from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):
    INIT_AMMUNITION = 100
    AMMO_PER_ATTACK = 25

    def __init__(self,name,health,hit_strength):
        super().__init__(name,health,hit_strength,self.INIT_AMMUNITION)

    def attack(self):
        self.ammunition -= self.AMMO_PER_ATTACK
        if self.ammunition < 0:
            self.ammunition = 0


