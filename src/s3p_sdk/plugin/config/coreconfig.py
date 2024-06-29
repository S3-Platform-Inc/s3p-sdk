import dataclasses

from .abc_object import AbcObject
from .type import SOURCE, FILE, MIXIN


@dataclasses.dataclass
class CoreConfig(AbcObject):
    reference: str
    type: str
    files: list[str]
    is_localstorage: bool

    def dict(self) -> dict:
        return {
            "reference": self.reference,
            "type": self.type,
            "filenames": self.files,
            "localstorage": self.is_localstorage,
        }
