from project.formula_teams.formula_team import FormulaTeam

class RedBullTeam(FormulaTeam):

    @property
    def expenses(self) -> int:
        return 250000

    @property

    def title_sponsor(self) -> dict:
        return {1:1500000,2:800000}

    @property
    def additional_sponsor(self) -> dict:
        return {8:20000,10:10000}


            
            







