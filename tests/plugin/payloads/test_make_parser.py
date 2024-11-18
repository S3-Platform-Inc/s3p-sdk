import logging

import pytest
import datetime

from s3p_sdk.plugin.payloads.parsers import S3PParserBase
from s3p_sdk.types import S3PRefer, S3PDocument
from s3p_sdk.plugin.config.type import SOURCE, ML

from tests.plugin.payloads.fixtures.refers import src_refer


class TestParserMaker:

    class MyParser(S3PParserBase):

        def __init__(self, refer: S3PRefer, max_docs: int = None, last_doc: S3PDocument = None):
            super().__init__(refer, max_docs, last_doc)

        def _parse(self) -> None:
            # HOST - это главная ссылка на источник, по которому будет "бегать" парсер
            self.logger.debug(F"Parser enter to {self._refer.to_logging}")

    def test_make_parser(self, src_refer):
        """Simple parser init"""
        m = self.MyParser(src_refer)

    def test_init_with_valid_max_docs(self, src_refer):
        """Simple parser init with valid max_docs"""
        assert self.MyParser(src_refer, max_docs=2)

    def test_init_with_null_max_docs(self, src_refer):
        """
        Simple parser init with zero value max_docs.
        Max_documents must be positive integer or None value.
        """
        try:
            self.MyParser(src_refer, max_docs=0)
        except AssertionError as e:
            assert True, e
        else:
            assert False, "max_documents must be positive integer or None value"

