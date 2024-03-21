from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import datetime


@dataclass
class S3PRefer:
    """
    Объект источника в SPP
    """
    id: int
    name: str | None
    type: str | None
    loaded: datetime | None
