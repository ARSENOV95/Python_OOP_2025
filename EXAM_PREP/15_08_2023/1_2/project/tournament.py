from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam


equipment_types= {"KneePad":KneePad,"ElbowPad":ElbowPad}
team_types= {"KneePad":KneePad,"ElbowPad":ElbowPad}


class Tournament:
    def __init__(self,name: str,capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment:list[BaseEquipment] = []
        self.teams:list[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value :str):
        if not (value.strip() != '' and value.isalnum()):
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self,equipment_type: str):
        if equipment_type not in equipment_types:
            raise Exception("Invalid equipment type!")

        I



    def add_team(self,team_type: str, team_name: str, country: str, advantage: int):
        pass

    def sell_equipment(self,equipment_type: str, team_name: str):
        pass

    def remove_team(self,team_name: str):
        pass

    def increase_equipment_price(self,equipment_type: str):
        pass

    def play(self,team_name1: str, team_name2: str):
        pass

    def get_statistics(self):
        pass