from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 120

    def __init__(self, name :str):
        super().__init__(name,oxygen_level=self.INITIAL_OXYGEN_LEVEL)

    def miss(self,time_to_catch: int):
        used_time = time_to_catch = time_to_catch * 0.6

        if self.oxygen_level - used_time >= 0:
            self.oxygen_level = round(self.oxygen_level - used_time)
        else:
            self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL

