from main import father
from project.father import Father
from project.mother import Mother


class Child(Father,Mother):
    def __init__(self,name :str,age :int,gender :str):
        Father.__init__(self)
        Mother.__init__(self)
        self.name = name
        self.age = age
        self.gender = gender

    def child_info(self):
        return f"{self.name}\n{self.age}\n{self.gender}"

