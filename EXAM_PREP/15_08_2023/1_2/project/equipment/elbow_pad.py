from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    BASE_PROTECTION = 90
    BASE_PRICE = 25.00
    PRICE_INCREASE = 0.10

    def __init__(self,):
        super().__init__(protection=self.BASE_PROTECTION,price=self.BASE_PRICE)

    def increase_price(self):
        self.price *= self.PRICE_INCREASE
