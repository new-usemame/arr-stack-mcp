from enum import Enum


class EntityHistoryEventType(str, Enum):
    ALBUMIMPORTINCOMPLETE = "albumImportIncomplete"
    ARTISTFOLDERIMPORTED = "artistFolderImported"
    DOWNLOADFAILED = "downloadFailed"
    DOWNLOADIGNORED = "downloadIgnored"
    DOWNLOADIMPORTED = "downloadImported"
    GRABBED = "grabbed"
    TRACKFILEDELETED = "trackFileDeleted"
    TRACKFILEIMPORTED = "trackFileImported"
    TRACKFILERENAMED = "trackFileRenamed"
    TRACKFILERETAGGED = "trackFileRetagged"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
