from abc import ABC, abstractmethod


class AbcParamConfig(ABC):
    key: str
    typeof: str
    value: object

    @abstractmethod
    def dict(self) -> dict: ...


__all__ = [
    "AbcParamConfig",
]
