from enum import Enum


class AllowFingerprinting(str, Enum):
    ALLFILES = "allFiles"
    NEVER = "never"
    NEWFILES = "newFiles"

    def __str__(self) -> str:
        return str(self.value)
