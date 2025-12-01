from project.song import Song

class Album:
    def __init__(self,name :str,song: Song): #songs is an object that can either be a list or none
        self.name = name
        self.songs:list[Song] = song
        self.published = False

    def add_song(self,song_name: Song) -> str:
        if self.published:
            return "Cannot add songs. Album is published."

        if song_name.single:
            return f"Cannot add {song_name.name}. It's a single"

        for song in self.songs:  #check if the current song name is in the list of song and if yes we skip adding it
            if song.name == song_name.name:
                return "Song is already in the album."

        self.songs.append(song_name)
        return  f"Song {song_name.name} has been added to the album {self.name}."

    def remove_song(self,song_name: str) -> str:
        rm_song = next((song for song in self.songs if song.name == song_name),None)

        if rm_song:
            if self.published:
                return "Cannot remove songs. Album is published."
            self.songs.remove(rm_song)
            return  f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        return f"Album {self.name}\n{'\n'.join(f'== {song.get_info()}' for song in self.songs)}"