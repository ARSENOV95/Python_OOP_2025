class ImageArea:
    def __init__(self,width :int,height :int):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    #the result of eq and ne will be the same so no need fro defining both
    def __eq__(self, other):
        return self.get_area() == other.get_area()


    #same as with eq and ne , when we have le, and we want gem python will do not __le__
    def __le__(self, other):
        return self.get_area() <= other.get_area()

    #same as above
    def __lt__(self, other):
        return self.get_area() < other.get_area()




a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)

print(a1 == a2)
print(a1 != a3)


a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)

print(a1 != a2)
print(a1 >= a3)


a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)

print(a1 <= a2)
print(a1 < a3)