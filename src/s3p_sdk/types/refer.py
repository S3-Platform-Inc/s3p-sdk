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

    @property
    def to_logging(self) -> str:
        """
        General string representation of the S3P document for logging purposes
        :return:
        """
        _id = ''
        if self.id:
            _id = f' | ID\'s: {self.id}'
        return f'S3P refer{_id} | name: {self.name} | type: {self.type}'
