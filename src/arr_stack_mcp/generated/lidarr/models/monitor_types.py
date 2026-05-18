from enum import Enum


class MonitorTypes(str, Enum):
    ALL = "all"
    EXISTING = "existing"
    FIRST = "first"
    FUTURE = "future"
    LATEST = "latest"
    MISSING = "missing"
    NONE = "none"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
