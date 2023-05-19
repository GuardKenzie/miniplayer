from mpd import MPDClient, ConnectionError, CommandError
from .config import Config
from PIL import Image
from io import BytesIO
from pathlib import Path

class Song:
    def __init__(self, song: dict):
        keys = song.keys()

        self.file = Path(song["file"])

        self.title        = song["title"]       if "title"       in keys else None
        self.artist       = song["artist"]      if "artist"      in keys else None
        self.album        = song["album"]       if "album"       in keys else None
        self.album_artist = song["albumartist"] if "albumartist" in keys else None

        self.pos = int(song["pos"])
        self.id  = int(song["id"])

    def printable_title(self) -> str:
        """
        A function that returns the title of the song if available,
        otherwise it returns the file name.
        """
        if self.title is not None:
            return self.title
        else:
            return self.file.name

    def __repr__(self) -> str:
        return f"Song(id={self.id}, pos={self.pos}, file={self.file})"

    def __eq__(self, other) -> bool:
        return self.pos == other.pos
    
    def __gt__(self, other) -> bool:
        return self.pos > other.pos

    def __lt__(self, other) -> bool:
        return self.pos < other.pos
    
    def __str__(self) -> str:
        title = self.printable_title()
        prefix = None

        if self.artist is not None:
            prefix = self.artist
        
        elif self.album_artist is not None:
            prefix = self.album_artist
        
        elif self.album is not None:
            prefix = self.album
        
        if prefix is not None:
            return f"{prefix} - {title}"
        else:
            return f"{title}"

class MPDInterface:
    def __init__(self):
        config = Config()
        
        self.host = config.mpd.get("host", "localhost")
        self.port = config.mpd.get("port", 6600)

        self.client = MPDClient()
        self.client.connect(self.host, self.port)


    @property
    def duration(self) -> float|None:

        if self.stopped:
            return None

        status = self.status
        return float(status["duration"])

    
    @property
    def ellapsed(self) -> float|None:

        if self.stopped:
            return None

        status = self.status
        return float(status["ellapsed"])


    @property
    def repeat(self) -> bool:
        status = self.status
        return status["repeat"] == "1"

    @repeat.setter
    def repeat(self, new_state: bool):
        try:
            self.client.repeat(str(int(new_state)))

        except ConnectionError:
            self._reconnect()
            self.repeat = new_state


    @property
    def volume(self) -> int:
        status = self.status
        return int(status["volume"])

    @volume.setter
    def volume(self, new_value: int):
        try:
            self.client.setvol(new_value)
        
        except ConnectionError:
            self._reconnect()
            self.volume = new_value


    @property
    def playing(self) -> bool:
        status = self.status
        return status["state"] == "play"


    @property
    def stopped(self) -> bool:
        status = self.status
        return status["state"] == "stopped"


    @property
    def status(self) -> dict:
        try:
            return self.client.status()

        except ConnectionError:
            self._reconnect()
            return self.status


    def _reconnect(self) -> None:
        """
        A function to try reconnecting to MPD
        """
        try:
            self.client.connect(self.host, self.port)
        except ConnectionError:
            print("Lost connection to MPD!")
    

    def _get_album_art(self) -> bytes:
        """
        This function returns the bytes data for the current songs
        album art
        """
        try:
            # Fetch album art data
            current_song_file = self.client.currentsong()["file"]
            return self.client.albumart(current_song_file)["binary"]
        except ConnectionError:
            # Lost connection so we try to reconnect and grab the art
            self._reconnect()
            return self._get_album_art()


    def albumart(self) -> Image.Image:
        """
        This function returns the album art image for the current song
        as a PIL Image object
        """

        album_art_data = self._get_album_art()

        # Wrap image data in BytesIO for PIL
        album_art_wrapper = BytesIO(album_art_data)
        return Image.open(album_art_wrapper)


    def toggle_playing(self) -> None:
        """
        A function that toggles the playing state of MPD
        """

        if self.playing:
            self.client.pause()
        else:
            self.client.play()

    
    def next(self) -> None:
        """
        A function that skips to the next song
        """

        try:
            self.client.next()
        except ConnectionError:
            self._reconnect()
            self.next()


    def previous(self) -> None:
        """
        A function that skips to the previous song
        """

        try:
            self.client.previous()
        except ConnectionError:
            self._reconnect()
            self.previous()
    

    @property
    def playlist(self) -> list[Song]:
        """
        A function that returns the playlist as a list of Song objects.
        """

        try:
            return sorted([Song(s) for s in self.client.playlistid()])
        except ConnectionError:
            self._reconnect()
            return self.playlist


    @property
    def current_song(self) -> dict:
        """
        The currently playing song. Equivalent to
        MPDClient.currentsong()
        """

        try:
            return Song(self.client.currentsong())
        except ConnectionError:
            self._reconnect()
            return self.current_song
        

    def clear_playlist(self):
        try:
            self.client.clear()
        except ConnectionError:
            self._reconnect()
            return self.clear_playlist()