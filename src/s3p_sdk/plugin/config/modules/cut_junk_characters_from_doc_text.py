"""CutJunkCharactersFromDocumentTextConfig module package"""
import dataclasses

from .abc_module import AbcModuleConfig
from s3p_sdk.module import CutJunkCharactersFromDocumentText


@dataclasses.dataclass
class CutJunkCharactersFromDocumentTextConfig(AbcModuleConfig):
    """Модуль, который очищает строковые поля материала от мусорных символов"""

    def __init__(self, order: int, is_critical: bool = False, p_fields: list[str] = None):
        assert isinstance(is_critical, bool)
        assert isinstance(order, int) and order > 0
        self._verify(p_fields)
        self.order = order
        self.name = CutJunkCharactersFromDocumentText
        self.is_critical = is_critical

        if p_fields:
            self.parameters = {
                'fields': p_fields,
            }
        else:
            self.parameters = None

    def _verify(self, fields: list[str]):
        assert ((fields
                 and isinstance(fields, list)
                 and all([isinstance(el, str) for el in fields])
                 )
                or fields is None
                )
        static_fields = ["text", "title", "abstract"]
        if fields:
            assert 0 <= len(fields) <= len(static_fields)
            print(fields)
            for field in fields:
                print(field)
                assert field in static_fields
