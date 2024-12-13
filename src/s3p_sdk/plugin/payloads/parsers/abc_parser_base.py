from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from s3p_sdk.types import S3PDocument, S3PPluginRestrictions


class AbcS3PParserExtends(metaclass=ABCMeta):
    """
    Abstract class as extends of the base payload for S3 plugins
    """

    _parsed_document: list[S3PDocument]
    _restriction: S3PPluginRestrictions

    @abstractmethod
    def content(self) -> tuple[S3PDocument, ...]:
        """
        Main parser's method that will be called by the S3P node.

        :return: tuple[S3PDocument, ...] - tuple of the parsed documents
        """
        ...

    @abstractmethod
    def _parse(self) -> None: ...

    @abstractmethod
    def _find(self, document: S3PDocument): ...

    ...
