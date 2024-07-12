"""Abstract module package"""
from s3p_sdk.plugin.config import AbcObject


class AbcModuleConfig(AbcObject):
    """
    Abstract base class for all modules
    """
    order: int
    name: str
    is_critical: bool
    parameters: dict | None

    def dict(self) -> dict:
        return {
            'order': self.order,
            'name': self.name,
            'critical': self.is_critical,
            'params': self.parameters if self.parameters else {},
        }
