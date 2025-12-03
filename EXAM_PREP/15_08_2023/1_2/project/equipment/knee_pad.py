from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    BASE_PROTECTION = 120
    BASE_PRICE = 15.00
    PRICE_INCREASE = 0.20

    def __init__(self,):
        super().__init__(protection=self.BASE_PROTECTION,price=self.BASE_PRICE)

    def increase_price(self):
        self.price *= self.PRICE_INCREASE
