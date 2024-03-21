from __future__ import annotations

from dataclasses import dataclass

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import S3PRefer


@dataclass
class S3PRole:
    """
    Объект роли в S3 Platform
    """
    id: int
    name: str | None
    sources: tuple[S3PRefer, ...] | None
