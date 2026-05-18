from enum import Enum


class ImportListType(str, Enum):
    ADVANCED = "advanced"
    LASTFM = "lastFm"
    OTHER = "other"
    PROGRAM = "program"
    SPOTIFY = "spotify"

    def __str__(self) -> str:
        return str(self.value)
