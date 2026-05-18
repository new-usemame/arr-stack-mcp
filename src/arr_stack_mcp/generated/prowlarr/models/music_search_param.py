from enum import Enum


class MusicSearchParam(str, Enum):
    ALBUM = "album"
    ARTIST = "artist"
    GENRE = "genre"
    LABEL = "label"
    Q = "q"
    TRACK = "track"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
