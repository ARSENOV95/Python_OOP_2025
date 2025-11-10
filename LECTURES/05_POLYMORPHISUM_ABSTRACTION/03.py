class Guitar:
    def play(self):
        return "Playing the guitar"


class Children:
   def play(self):
       return "Children are playing"

guitar = Guitar()
children = Children()


def start_playing(inst):
    return inst.play()


print(start_playing(children))
print(start_playing(guitar))