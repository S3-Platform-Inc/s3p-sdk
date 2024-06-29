__all__ = ['EntryConfig', 'AbcParamConfig', 'ModuleParamConfig', 'ConstParamConfig']

import dataclasses

from s3p_sdk.plugin.config import AbcObject
from .abc_param import AbcParamConfig
from .module_param_config import ModuleParamConfig
from .const_param_config import ConstParamConfig


@dataclasses.dataclass
class EntryConfig(AbcObject):
    method: str
    params: list[AbcParamConfig]

    def dict(self) -> dict:
        return {
            'point': self.method,
            'params': [param.dict() for param in self.params]
        }
