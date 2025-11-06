from pandas.io.formats.info import series_sub_kwargs


class PhotoAlbum:
    def __init__(self,pages :int,photos_count = 4):
        self.pages = pages
        self.photos:list = [[] for _ in range(self.pages)]
        self.photos_count = photos_count

    @classmethod
    def from_photos_count(cls,pages : int,photos_count: int):
        if photos_count < 4:
            photos_count = 4
        return cls(pages,photos_count)


    def add_photo(self,label: str):
        page = 0
        position = 0
        for i in range(len(self.photos)):
            if len(self.photos[i]) < self.photos_count:
                self.photos[i].append(label)
                page = i + 1
                position = self.photos[i].index(label) + 1
                break

        return f"{label} photo added successfully on page {page} slot {position}"

    def display(self):
        photo_album = [[] for _ in self.photos]






album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())