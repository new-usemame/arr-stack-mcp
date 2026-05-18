from enum import Enum


class BookSearchParam(str, Enum):
    AUTHOR = "author"
    GENRE = "genre"
    PUBLISHER = "publisher"
    Q = "q"
    TITLE = "title"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
