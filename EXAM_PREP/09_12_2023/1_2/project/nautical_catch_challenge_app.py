from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish

diver_types = {"FreeDiver":FreeDiver,"ScubaDiver":ScubaDiver}
fish_types = {"PredatoryFish":PredatoryFish,"DeepSeaFish":DeepSeaFish}


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers:list[BaseDiver] = []
        self.fish_list: list[BaseFish] = []

    def dive_into_competition(self,diver_type: str, diver_name: str):
        if diver_type not in diver_types:
            return f"{diver_type} is not allowed in our competition."

        diver = self.diver_name_exists(diver_name)

        if diver:
            return f"{diver_name} is already a participant."

        diver = diver_types[diver_type](diver_name)
        self.divers.append(diver)

        return f"{diver_name} is successfully registered for the competition as a {diver_type}."


    def swim_into_competition(self,fish_type: str, fish_name: str, points: float):
        if fish_type not in fish_types:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish = self.fish_name_exists(fish_name)

        if fish:
            return f"{fish_name} is already permitted."

        fish = fish_types[fish_type](fish_name,points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."


    def chase_fish(self,diver_name: str, fish_name: str, is_lucky: bool):
        diver = self.diver_name_exists(diver_name)

        if not diver:
            return f"{diver_name} is not registered for the competition."

        fish = self.fish_name_exists(fish_name)

        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."


        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."


        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver.name} hits a {fish.points:.1f}pt. {fish.name}."
            else:
                diver.miss(fish.time_to_catch)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} missed a good {fish_name}."

        else:
            diver.hit(fish)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver.name} hits a {fish.points:.1f}pt. {fish.name}."


    def health_recovery(self):
        injured_divers = 0

        for diver in self.divers:
            if diver.has_health_issue:
                injured_divers += 1
                diver.update_health_status()
                diver.renew_oxy()


        return  f"Divers recovered: {injured_divers}"



    def diver_catch_report(self,diver_name: str):
        diver = self.diver_name_exists(diver_name)
        result = ''

        if diver is None:
            return result

        result = f"**{diver.name} Catch Report**\n"
        result += '\n'.join(fish.fish_details() for fish in diver.catch) if diver.catch else ''

        return result.strip()


    def competition_statistics(self):
        sorted_divers:list[BaseDiver] = sorted(self.divers,key = lambda d:(-d.competition_points,-len(d.catch),d.name))


        stats = f'**Nautical Catch Challenge Statistics**\n'
        stats += '\n'.join(str(diver) for diver in sorted_divers if not diver.has_health_issue)

        return stats.strip()





    #HELPERS
    def diver_name_exists(self,name):
        return next((diver for diver in self.divers if diver.name == name),None)

    def fish_name_exists(self,name):
        return next((fish for fish in self.fish_list if fish.name == name),None)