from dataclasses import dataclass


@dataclass
class S3PNode:
    """
    Структура узла платформы.
    """
    id: int | None
    name: str
    ip: str | None
    config: dict
    session: int | None
