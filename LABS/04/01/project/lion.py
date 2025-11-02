from project.animal import Animal


class Lion(Animal):
    MONEY = 50
    def __init__(self,name,gender,age):
        super().__init__(name,gender,age,self.MONEY)

