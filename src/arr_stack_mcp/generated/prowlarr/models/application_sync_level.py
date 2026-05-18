from enum import Enum


class ApplicationSyncLevel(str, Enum):
    ADDONLY = "addOnly"
    DISABLED = "disabled"
    FULLSYNC = "fullSync"

    def __str__(self) -> str:
        return str(self.value)
