from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak

climber_mapper = {"ArcticClimber":ArcticClimber
                  ,"SummitClimber":SummitClimber
                  }

peak_mapper = {"ArcticPeak":ArcticPeak
               ,"SummitPeak":SummitPeak
               }


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers: list[BaseClimber] = []
        self.peaks: list[BasePeak] = []

    def check_climber_exists(self,name):
        return next((climber for climber in self.climbers if climber.name == name),None)

    def check_peak_exists(self,name):
        return next((peak for peak in self.peaks if peak.name == name),None)


    def register_climber(self,climber_type: str, climber_name: str):
        if climber_type not in climber_mapper.keys():
            return f"{climber_type} doesn't exist in our register."

        climber = self.check_climber_exists(climber_name)

        if climber is not None:
            return f"{climber_name} has been already registered."

        climber = climber_mapper[climber_type](climber_name)

        self.climbers.append(climber)
        return f"{climber_name} is successfully registered as a {climber_type}."


    def peak_wish_list(self,peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in peak_mapper:
            return  f"{peak_type} is an unknown type of peak."

        peak = peak_mapper[peak_type](peak_name,peak_elevation)
        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."


    def check_gear(self,climber_name: str, peak_name: str, gear: list[str]):
        climber = self.check_climber_exists(climber_name)
        peak = self.check_peak_exists(peak_name)

        missing_gear = [item for item in peak.get_recommended_gear() if item not in gear]
        missing_gear = sorted(missing_gear)

        if len(missing_gear) > 1:
            climber.is_prepared = False
            return f"{climber.name} is not prepared to climb {peak.name}. Missing gear: {', '.join(missing_gear)}."

        return f"{climber.name} is prepared to climb {peak.name}."

    def perform_climbing(self,climber_name: str, peak_name: str):
        climber = self.check_climber_exists(climber_name)
        peak = self.check_peak_exists(peak_name)


        if climber is None:
            return f"Climber {climber_name} is not registered yet."

        if peak is None:
            return f"Peak {peak_name} is not part of the wish list."


        if climber.is_prepared and climber.can_climb():
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."


        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics (self):
        sorted_climbers = sorted([climber for climber in self.climbers if climber.conquered_peaks],key = lambda c: (-len(c.conquered_peaks),c.name))


        stats = f"Total climbed peaks: {len(self.peaks)}\n**Climber's statistics:**\n"
        stats += '\n'.join(str(climber) for climber in sorted_climbers)

        return stats.strip()