from project.formula_teams.formula_team import FormulaTeam

class MercedesTeam(FormulaTeam):
      
    @property
    def expenses(self) -> int:
        return 200000

    @property

    def title_sponsor(self) -> dict:
        return {1:1000000,3:500000}

    @property
    def additional_sponsor(self) -> dict:
        return {5:100000,7:50000}


