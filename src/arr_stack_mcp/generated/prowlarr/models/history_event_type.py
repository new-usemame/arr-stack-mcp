from enum import Enum


class HistoryEventType(str, Enum):
    INDEXERAUTH = "indexerAuth"
    INDEXERINFO = "indexerInfo"
    INDEXERQUERY = "indexerQuery"
    INDEXERRSS = "indexerRss"
    RELEASEGRABBED = "releaseGrabbed"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
