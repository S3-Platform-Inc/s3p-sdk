import dataclasses

from .abc_object import AbcObject
from .restrictconfig import RestrictionsConfig


@dataclasses.dataclass
class CoreConfig(AbcObject):
    reference: str
    type: str
    files: list[str]
    is_localstorage: bool
    restrictions: RestrictionsConfig

    def dict(self) -> dict:
        return {
            "reference": self.reference,
            "type": self.type,
            "filenames": self.files,
            "localstorage": self.is_localstorage,
            "restrictions": self.restrictions.dict(),
        }
