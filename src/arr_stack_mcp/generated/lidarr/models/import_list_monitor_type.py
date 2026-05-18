from enum import Enum


class ImportListMonitorType(str, Enum):
    ENTIREARTIST = "entireArtist"
    NONE = "none"
    SPECIFICALBUM = "specificAlbum"

    def __str__(self) -> str:
        return str(self.value)
