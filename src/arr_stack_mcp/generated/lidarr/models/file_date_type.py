from enum import Enum


class FileDateType(str, Enum):
    ALBUMRELEASEDATE = "albumReleaseDate"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
