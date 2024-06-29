__all__ = [
    'SCHEDULE',
    'TriggerConfig',
]

import dataclasses
from datetime import timedelta

from .abc_object import AbcObject

SCHEDULE: str = "SCHEDULE"


@dataclasses.dataclass
class TriggerConfig(AbcObject):
    type: str
    interval: timedelta

    def dict(self) -> dict:
        return {
            "type": self.type,
            "interval": f'{int(self.interval.total_seconds())} seconds'
        }
