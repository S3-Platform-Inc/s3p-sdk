__all__ = [
    "ModuleParamConfig",
]

import dataclasses
from .abc_param import AbcParamConfig
from s3p_sdk.module import names as m_names


@dataclasses.dataclass
class ModuleParamConfig(AbcParamConfig):
    """
    Объект параметра с типом "модуль"
    """
    key: str
    module_name: str
    is_use_bus: bool
    typeof: str = 'module'

    def __init__(self, key: str, module_name: str, bus: bool):
        assert isinstance(key, str) and len(key) > 0
        assert isinstance(module_name, str) and module_name in m_names
        assert isinstance(bus, bool)
        self.key = key
        self.module_name = module_name
        self.is_use_bus = bus

    def dict(self) -> dict:
        return {
            'key': self.key,
            'value': {
                'type': self.typeof,
                'name': str(self.module_name),
                'bus': bool(self.is_use_bus),
            }
        }

