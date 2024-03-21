import datetime
from dataclasses import dataclass


@dataclass
class S3PExport:
    """
    Структура узла платформы.
    """
    id: int
    date: datetime.datetime
    params: dict | None
    count: int | None
