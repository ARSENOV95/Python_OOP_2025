from abc import  ABC,abstractmethod

class FormulaTeam(ABC):
    def __init__(self,budget :int):
        self.__budget = budget


    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.budget = value




    @property
    @abstractmethod
    def expenses(self) -> int:
        pass

    @property
    @abstractmethod
    def title_sponsor(self) -> dict:
        pass

    @property
    @abstractmethod
    def additional_sponsor(self) -> dict:
        pass

    def calculate_revenue_after_race(self,race_pos: int):
        revenue = 0
   
        if race_pos <= 3:
            if self.title_sponsor.get(race_pos):
                revenue += self.title_sponsor[race_pos] 
            else:
                revenue += min(self.title_sponsor.values())
            revenue +=  max(self.additional_sponsor.values())

        elif race_pos > 3:
            if self.additional_sponsor.get(race_pos):
                revenue += self.additional_sponsor[race_pos]
            
            elif race_pos < min(self.additional_sponsor.values()):
                revenue +=  max(self.additional_sponsor.values())

            elif  min(self.additional_sponsor.values()) < race_pos <  max(self.additional_sponsor.values()):
                revenue += min(self.additional_sponsor.values())

        revenue -= self.expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

            
