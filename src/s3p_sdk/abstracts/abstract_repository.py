from abc import ABC, abstractmethod
from pathlib import Path

from multipledispatch import dispatch

from s3p_sdk.types import S3PPlugin, S3PDocument


class AbstaractRepository(ABC):
    _plugin: S3PPlugin

    @dispatch(S3PDocument)
    @abstractmethod
    def has(self, document: S3PDocument) -> bool:
        ...

    @dispatch(S3PDocument, str)
    @abstractmethod
    def has(self, document: S3PDocument, asset: str) -> bool:
        ...

    @abstractmethod
    def open(self, document: S3PDocument, filename: str, **kwargs):
        ...

    @abstractmethod
    def dir_of(self, document: S3PDocument) -> Path:
        ...

    @abstractmethod
    def path_for(self, document: S3PDocument, asset: str) -> Path:
        ...
