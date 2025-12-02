from project.collectors.base_collector import BaseCollector


class PrivateCollector(BaseCollector):
    INITIAL_AVAILABLE_MONEY:float = 25000.0
    INITIAL_AVAILABLE_SPACE:int = 3000
    MONEY_INCREASE = 5000.0

    def __init__(self,name):
        super().__init__(name,self.INITIAL_AVAILABLE_MONEY,self.INITIAL_AVAILABLE_SPACE)

    def increase_money(self):
        self.available_money += self.MONEY_INCREASE