import dataclasses

from .abc_object import AbcObject
from s3p_sdk.plugin.config.modules import AbcModuleConfig


@dataclasses.dataclass
class MiddlewareConfig(AbcObject):
    modules: list[AbcModuleConfig]
    bus: object | None

    def dict(self) -> dict:
        return {
            'modules': [module.dict() for module in self.modules],
        }
