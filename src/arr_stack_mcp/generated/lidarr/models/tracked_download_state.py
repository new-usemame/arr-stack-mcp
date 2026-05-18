from enum import Enum


class TrackedDownloadState(str, Enum):
    DOWNLOADFAILED = "downloadFailed"
    DOWNLOADFAILEDPENDING = "downloadFailedPending"
    DOWNLOADING = "downloading"
    IGNORED = "ignored"
    IMPORTBLOCKED = "importBlocked"
    IMPORTED = "imported"
    IMPORTFAILED = "importFailed"
    IMPORTING = "importing"
    IMPORTPENDING = "importPending"

    def __str__(self) -> str:
        return str(self.value)
