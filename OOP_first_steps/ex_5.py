class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


song = Music("Title", "Artist")
print(song.print_info())
print(song.play())

song2 = Music("Awake", "Godsmack", "for you I am awake...")
print(song2.print_info())
print(song2.play())
