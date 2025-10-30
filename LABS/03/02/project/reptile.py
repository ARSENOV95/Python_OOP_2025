from project.animal import Animal


class Reptile(Animal):
    def __init__(self,name :str):
        Animal.__init__(self,name)
