from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):
    GEAR = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def get_recommended_gear(self):
        return  self.GEAR

    def calculate_difficulty_level(self):
        if self.elevation > 2500:
            return "Extreme"
        if  1500 <= self.elevation <= 2500:
            return "Advanced"

