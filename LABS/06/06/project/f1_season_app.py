from project.formula_teams.red_bull_team import RedBullTeam
from project.formula_teams.mercedes_team import MercedesTeam

class F1SeasonApp:
    def __init__(self):
        self.red_bull_team: RedBullTeam = None
        self.mercedes_team: MercedesTeam = None


    def register_team_for_season(self, team_name: str, budget: int):
        if not team_name in ('Red Bull','Mercedes'):
            raise ValueError("Invalid team name!")

        if team_name == 'Red Bull':
            self.red_bull_team = RedBullTeam(budget)
        else:
            self.mercedes_team = MercedesTeam(budget)

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self,race_name: str, red_bull_pos: int, mercedes_pos: int):
        if self.red_bull_team is None or self.mercedes_team is None:
            raise Exception("Not all teams have registered for the season.")

        rb_revenue = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mb_revenue = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)


        return f"Red Bull: {rb_revenue}. Mercedes: {mb_revenue}. {'Red Bull' if red_bull_pos < mercedes_pos else 'Mercedes'} is ahead at the {race_name} race."