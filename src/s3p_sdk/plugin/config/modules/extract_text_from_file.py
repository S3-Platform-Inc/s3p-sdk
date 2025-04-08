"""ExtractTextFromFile module package"""
import dataclasses

from .abc_module import AbcModuleConfig
from s3p_sdk.module import ExtractTextFromFile as MNAME


@dataclasses.dataclass
class ExtractTextFromFile(AbcModuleConfig):
    """

    """

    def __init__(self, order: int, is_critical: bool = False, storage: str = None):
        assert isinstance(is_critical, bool)
        assert isinstance(order, int) and order > 0
        self._verify(storage)

        self.order = order
        self.name = MNAME
        self.is_critical = is_critical

        if storage:
            self.parameters = {
                'storage': storage,
            }
        else:
            self.parameters = None

    def _verify(self, storage: str):
        assert isinstance(storage, str) or storage is None
        storage_stage = ["temporary", "localstorage", "fileserver"]
        if storage:
            assert storage in storage_stage
