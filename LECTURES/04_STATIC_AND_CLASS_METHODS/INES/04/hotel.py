from project.r
class Hotel:
    def __init__(self,name :str):
        self.name = name
        self.rooms: list[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls,stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self,room: Room):
        if room not in self.rooms:
            self.rooms.append(room)
        return None

    def take_room(self,room_number, people):
        room = next((r for r in self.rooms if r.),None)