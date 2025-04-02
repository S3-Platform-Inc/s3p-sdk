import pytest

from multipledispatch import dispatch

from s3p_sdk.abstracts.abstract_repository import AbstaractRepository
from s3p_sdk.types import S3PPlugin, S3PDocument


class Repository(AbstaractRepository):

    @dispatch(S3PDocument)
    def has(self, document: S3PDocument) -> bool:
        ...

    @dispatch(S3PDocument, str)
    def has(self, document: S3PDocument, asset: str) -> bool:
        ...

    def open(self, document: S3PDocument, filename: str, **kwargs):
        ...


class TestAbstaractRepository():
    _plugin: S3PPlugin

    def test_subclass(self):
        r = Repository()
        assert r
