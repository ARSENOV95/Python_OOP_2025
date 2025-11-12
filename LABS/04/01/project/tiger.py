from project.animals.animal import Animal


class Tiger(Animal):
    MONEY = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.MONEY)

