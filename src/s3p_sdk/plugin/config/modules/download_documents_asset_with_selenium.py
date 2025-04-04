"""DownloadDocumentsAssetWithSelenium module package"""
import dataclasses

from .abc_module import AbcModuleConfig
from s3p_sdk.module import DownloadDocumentsAssetWithSelenium as MNAME


@dataclasses.dataclass
class DownloadDocumentsAssetWithSelenium(AbcModuleConfig):
    """Модуль, который очищает строковые поля материала от мусорных символов"""

    def __init__(self, order: int, available_field: str, is_critical: bool = False, cookie_selector: str = None):
        assert isinstance(is_critical, bool)
        assert isinstance(order, int) and order > 0
        assert isinstance(available_field, str)
        assert isinstance(cookie_selector, str) or cookie_selector is None
        self.order = order
        self.name = MNAME
        self.is_critical = is_critical
        self.parameters = {
            'available_field': available_field,
            'cookie_selector': cookie_selector,
        }
