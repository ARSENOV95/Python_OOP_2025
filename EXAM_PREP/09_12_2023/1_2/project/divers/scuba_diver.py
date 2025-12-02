from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        time_to_catch = time_to_catch * 0.3

        # TODO:Check logic test case value - 0,9
        if self.oxygen_level < time_to_catch:
            self.oxygen_level = 0

        self.oxygen_level = round(self.oxygen_level - time_to_catch)

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL

