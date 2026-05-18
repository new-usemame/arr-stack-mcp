from enum import Enum


class WriteAudioTagsType(str, Enum):
    ALLFILES = "allFiles"
    NEWFILES = "newFiles"
    NO = "no"
    SYNC = "sync"

    def __str__(self) -> str:
        return str(self.value)
