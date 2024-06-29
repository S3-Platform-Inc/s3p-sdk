__all__ = ['PayloadConfig', 'entry']

import dataclasses

from s3p_sdk.plugin.config import AbcObject
from .entry import EntryConfig


@dataclasses.dataclass
class PayloadConfig(AbcObject):
    file: str
    classname: str
    entry: EntryConfig

    def dict(self) -> dict:
        return {
            'file': self.file,
            'class': self.classname,
            'entry': self.entry.dict(),
        }
