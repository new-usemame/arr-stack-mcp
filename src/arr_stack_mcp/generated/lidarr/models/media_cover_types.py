from enum import Enum


class MediaCoverTypes(str, Enum):
    BANNER = "banner"
    CLEARLOGO = "clearlogo"
    COVER = "cover"
    DISC = "disc"
    FANART = "fanart"
    HEADSHOT = "headshot"
    LOGO = "logo"
    POSTER = "poster"
    SCREENSHOT = "screenshot"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
