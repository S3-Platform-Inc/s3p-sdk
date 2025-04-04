"""DownloadDocumentsAssetWithSelenium module package"""
import dataclasses

from .abc_module import AbcModuleConfig
from s3p_sdk.module import DownloadDocumentsAssetWithSelenium as MNAME


@dataclasses.dataclass
class DownloadDocumentsAssetWithSelenium(AbcModuleConfig):
    """Модуль, который очищает строковые поля материала от мусорных символов"""

    def __init__(self, order: int, is_critical: bool = False):
        assert isinstance(is_critical, bool)
        assert isinstance(order, int) and order > 0
        self.order = order
        self.name = MNAME
        self.is_critical = is_critical
