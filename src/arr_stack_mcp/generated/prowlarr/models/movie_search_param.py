from enum import Enum


class MovieSearchParam(str, Enum):
    DOUBANID = "doubanId"
    GENRE = "genre"
    IMDBID = "imdbId"
    IMDBTITLE = "imdbTitle"
    IMDBYEAR = "imdbYear"
    Q = "q"
    TMDBID = "tmdbId"
    TRAKTID = "traktId"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
