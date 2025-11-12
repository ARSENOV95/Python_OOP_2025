from project.formula_teams.formula_team import FormulaTeam

class MercedesTeam(FormulaTeam):
    RACE_EXPENSES = 200000

    def __init__(self,budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self,race_pos: int):
        revenue = 0
        sponsors = {'Petronas':{1:1000000,3:500000},'TeamViewer':{5:100000,7: 50000}}

        for sponsor,prize in sponsors.items():
            for prize_pos,prize_purse in prize:
                if race_pos == prize_pos:
                    revenue += prize_purse
                elif race_pos < prize_pos and race_pos != 1:
                    revenue += min(prize.values())

        revenue -= self.RACE_EXPENSES
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

