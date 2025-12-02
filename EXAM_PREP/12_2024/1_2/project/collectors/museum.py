from project.collectors.base_collector import BaseCollector

class Museum(BaseCollector):
    INITIAL_AVAILABLE_MONEY:float = 15000.0
    INITIAL_AVAILABLE_SPACE:int = 2000
    MONEY_INCREASE = 1000.0

    def __init__(self,name):
        super().__init__(name,self.INITIAL_AVAILABLE_MONEY,self.INITIAL_AVAILABLE_SPACE)

    def increase_money(self):
        self.available_money += self.MONEY_INCREASE
