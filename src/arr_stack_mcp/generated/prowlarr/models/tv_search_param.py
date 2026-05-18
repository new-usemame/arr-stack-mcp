from enum import Enum


class TvSearchParam(str, Enum):
    DOUBANID = "doubanId"
    EP = "ep"
    GENRE = "genre"
    IMDBID = "imdbId"
    Q = "q"
    RID = "rId"
    SEASON = "season"
    TMDBID = "tmdbId"
    TRAKTID = "traktId"
    TVDBID = "tvdbId"
    TVMAZEID = "tvMazeId"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
