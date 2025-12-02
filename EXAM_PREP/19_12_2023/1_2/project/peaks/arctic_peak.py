from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    GEAR = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def get_recommended_gear(self):
        return self.GEAR

    def calculate_difficulty_level(self)->str|None:
        if self.elevation > 3000:
            return "Extreme"
        if  2000 <= self.elevation <= 3000:
            return "Advanced"

