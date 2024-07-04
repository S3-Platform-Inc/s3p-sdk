__all__ = [
    "ConstParamConfig",
]

import dataclasses

from .abc_param import AbcParamConfig


@dataclasses.dataclass
class ConstParamConfig(AbcParamConfig):
    """
    Объект параметра с типом "модуль"
    """
    key: str
    value: str | int | float | list | dict
    typeof: str = 'const'

    def __init__(self, key: str, value: str | int | float | list | dict):
        assert isinstance(key, str) and len(key) > 0
        assert type(value) in (int, float, list, dict, str)
        self.key = key
        self.value = value

    def dict(self) -> dict:
        return {
            'key': self.key,
            'value': {
                'type': self.typeof,
                'value': self.value,
            }
        }

