import dataclasses

from .abc_module import AbcModuleConfig
from s3p_sdk.module import CutJunkCharactersFromDocumentText

@dataclasses.dataclass
class CutJunkCharactersFromDocumentTextConfig(AbcModuleConfig):

    def __init__(self, order: int, is_critical: bool = False, p_fields: list[str] = None):
        self.order = order
        self.name = CutJunkCharactersFromDocumentText
        self.is_critical = is_critical

        if p_fields:
            self.parameters = {
                'fields': p_fields,
            }
        else:
            self.parameters = None
