import dataclasses

from .trigger import TriggerConfig
from .abc_object import AbcObject


@dataclasses.dataclass
class TaskConfig(AbcObject):
    trigger: TriggerConfig

    def dict(self) -> dict:
        return {
            "trigger": self.trigger.dict(),
        }
