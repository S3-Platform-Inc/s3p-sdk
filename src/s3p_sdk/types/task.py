from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import S3PPlugin, S3PRefer


@dataclass
class S3PTask:
    """
    Структура Задачи S3 Platform.
    """
    id: int
    session_id: int
    status: int | None
    plugin: S3PPlugin
    refer: S3PRefer
