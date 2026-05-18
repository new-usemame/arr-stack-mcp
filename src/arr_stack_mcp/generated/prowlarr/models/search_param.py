from enum import Enum


class SearchParam(str, Enum):
    Q = "q"

    def __str__(self) -> str:
        return str(self.value)
