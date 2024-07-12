"""SaveDocument module package"""
import dataclasses

from .abc_module import AbcModuleConfig
from s3p_sdk.module import SaveDocument as mSaveDocument


@dataclasses.dataclass
class SaveDocument(AbcModuleConfig):
    """
    Модуль сохраняет все материалы из шины в базу данных S3P
    """

    def __init__(self, order: int, is_critical: bool = False):
        assert isinstance(is_critical, bool)
        assert isinstance(order, int) and order > 0
        self.order = order
        self.name = mSaveDocument
        self.is_critical = is_critical
        self.parameters = None
