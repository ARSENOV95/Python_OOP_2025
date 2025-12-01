from project.album import Album

class Band:
    def __init__(self,name :str,%):
        self.name = name
        self.albums:list[Album] = []

    def add_album(self,album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self,album_name: str):
        album = next((alb for alb in self.albums if alb.name == album_name),None)

        if album:
            if album.published:
                return f"Album has been published. It cannot be removed."
            self.albums.remove(album)
            return f"Album {self.name} has been removed."
        return "Album {name} is not found."

    def details(self):
        return f"Band {self.name}\n{'\n'.join(alb.details() for alb in self.albums)}"