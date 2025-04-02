from abc import ABC, abstractmethod
from multipledispatch import dispatch

from s3p_sdk.types import S3PPlugin, S3PDocument


class AbstaractRepository(ABC):
    _plugin: S3PPlugin

    @abstractmethod
    @dispatch(S3PDocument)
    def has(self, document: S3PDocument) -> bool:
        ...

    @abstractmethod
    @dispatch(S3PDocument, str)
    def has(self, document: S3PDocument, asset: str) -> bool:
        ...

    @abstractmethod
    def open(self, document: S3PDocument, filename: str, **kwargs):
        ...
