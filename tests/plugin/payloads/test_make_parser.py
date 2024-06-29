import logging

import pytest
import datetime

from s3p_sdk.plugin.payloads.parsers import S3PParserBase
from s3p_sdk.types import S3PRefer


class TestParserMaker:

    class MyParser(S3PParserBase):

        def __init__(self, refer: S3PRefer, ):
            super().__init__(refer)

        def _parse(self) -> None:
            # HOST - это главная ссылка на источник, по которому будет "бегать" парсер
            self.logger.debug(F"Parser enter to {self._refer.to_logging}")

    def test_make_parser(self, caplog):
        ref = S3PRefer(1, "test ref 1", "SOURCE", None)

        m = self.MyParser(ref)
