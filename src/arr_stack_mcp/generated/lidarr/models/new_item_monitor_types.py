from enum import Enum


class NewItemMonitorTypes(str, Enum):
    ALL = "all"
    NEW = "new"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
