from enum import Enum


class ArtistStatusType(str, Enum):
    CONTINUING = "continuing"
    DELETED = "deleted"
    ENDED = "ended"

    def __str__(self) -> str:
        return str(self.value)
