import dataclasses
from datetime import datetime

from .abc_object import AbcObject
from ...types import S3PDocument


@dataclasses.dataclass
class RestrictionsConfig(AbcObject):
    maximum_materials: int | None
    to_last_material: bool | None
    from_date: datetime | None
    to_date: datetime | None

    def dict(self) -> dict:
        return {
            "max_materials": self.maximum_materials,
            "last_material": self.to_last_material,
            "from_date": self.from_date.isoformat() if self.from_date else None,
            "to_date": self.to_date.isoformat() if self.to_date else None,
        }
