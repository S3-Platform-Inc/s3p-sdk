"""FilterOnlyNewDocumentWithDB module package"""
import dataclasses

from .abc_module import AbcModuleConfig
from s3p_sdk.module import FilterOnlyNewDocumentWithDB


@dataclasses.dataclass
class FilterOnlyNewDocumentWithDB(AbcModuleConfig):
    """
    Модуль фильтрует материалы плагина по признаку новизны.
    Новый материал - это материал, которого нет в базе данных S3P
    """

    def __init__(self, order: int, is_critical: bool = False):
        assert isinstance(is_critical, bool)
        assert isinstance(order, int) and order > 0
        self.order = order
        self.name = FilterOnlyNewDocumentWithDB
        self.is_critical = is_critical
        self.parameters = None
