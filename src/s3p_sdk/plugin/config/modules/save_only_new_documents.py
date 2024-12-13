"""SaveOnlyNewDocuments module package"""
import dataclasses

from .abc_module import AbcModuleConfig
from s3p_sdk.module import SaveOnlyNewDocuments as MNAME


@dataclasses.dataclass
class SaveOnlyNewDocuments(AbcModuleConfig):
    """The module checks for existing documents and then saves only the new ones"""

    def __init__(self, order: int, is_critical: bool = False):
        assert isinstance(is_critical, bool)
        assert isinstance(order, int) and order > 0
        self.order = order
        self.name = MNAME
        self.is_critical = is_critical
        self.parameters = None
