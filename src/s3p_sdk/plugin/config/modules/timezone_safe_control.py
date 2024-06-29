import dataclasses

from .abc_module import AbcModuleConfig
from s3p_sdk.module import TIMEZONESAFECONTROL


@dataclasses.dataclass
class TimezoneSafeControlConfig(AbcModuleConfig):

    def __init__(self, order: int, is_critical: bool = False, p_fields: list[str] = None):
        assert isinstance(is_critical, bool)
        assert isinstance(order, int) and order > 0
        assert ((p_fields
                and isinstance(p_fields, list)
                and all([isinstance(el, str) for el in p_fields])
                 )
                or p_fields is None
                )
        self.order = order
        self.name = TIMEZONESAFECONTROL
        self.is_critical = is_critical

        if p_fields:
            self.parameters = {
                'fields': p_fields,
            }
        else:
            self.parameters = None
