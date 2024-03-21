from __future__ import annotations

from dataclasses import dataclass

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from . import S3PRole


@dataclass
class S3PUser:
    """
    Объект пользователя в SPP
    """
    id: int
    name: str | None
    privilege: dict | None
    roles: tuple[S3PRole, ...] | None
