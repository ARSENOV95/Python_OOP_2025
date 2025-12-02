from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200
    STRENGTH_TO_CLIMB = 100

    def __init__(self,name :str):
        super().__init__(name,self.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= self.STRENGTH_TO_CLIMB

    def climb(self,peak : BasePeak):
        strength_per_climb = 20

        if peak.difficulty_level == 'Extreme':
           strength_per_climb *= 2
        else:
           strength_per_climb *=  1.5

        self.strength -= strength_per_climb
        self.conquered_peaks.append(peak)

