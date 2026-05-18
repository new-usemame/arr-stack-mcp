from enum import Enum


class IndexerPrivacy(str, Enum):
    PRIVATE = "private"
    PUBLIC = "public"
    SEMIPRIVATE = "semiPrivate"

    def __str__(self) -> str:
        return str(self.value)
