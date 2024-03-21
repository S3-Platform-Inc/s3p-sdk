import datetime
from dataclasses import dataclass


@dataclass
class S3PDigest:
    """
    Структура узла платформы.
    """
    id: int
    date: datetime.datetime
    comment: str | None = None
