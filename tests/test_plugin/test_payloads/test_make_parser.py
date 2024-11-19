import logging
import random
from configparser import Error

import pytest
import datetime

from s3p_sdk.exceptions.parser import S3PPluginPayloadError
from s3p_sdk.plugin.payloads.parsers import S3PParserBase
from s3p_sdk.types import S3PRefer, S3PDocument, S3PPlugin

from tests.test_plugin.test_payloads.fixtures.plugins import fix_plugin
from tests.test_plugin.test_payloads.fixtures.refers import src_refer
from tests.test_plugin.test_payloads.utils.test_doc import random_doc


@pytest.mark.payload_set
class TestParserMaker:

    class MyParser(S3PParserBase):

        def __init__(self, refer: S3PRefer, plugin: S3PPlugin, count: int, max_docs: int = None, last_doc: S3PDocument = None, with_error: bool = False, with_last_doc: S3PDocument | None = None):
            super().__init__(refer, plugin, max_docs, last_doc)
            self._count = count
            self.with_error = with_error
            self._with_last_doc = with_last_doc

        def _parse(self) -> None:
            # HOST - это главная ссылка на источник, по которому будет "бегать" парсер
            self.logger.debug(F"Parser enter to {self._refer.to_logging}")
            for i in range(self._count):
                if self.with_error and random.randint(0, int(self._count / 2)) >= i:
                    raise S3PPluginPayloadError(self._plugin, "Some random error")
                if self._with_last_doc is not None and int(self._count / 2) >= i:
                    self._find(self._with_last_doc)
                self._find(random_doc())

    def test_make_parser(self, src_refer, fix_plugin):
        """Simple parser init"""
        m = self.MyParser(src_refer, fix_plugin, 5)
        assert True

    def test_init_with_valid_max_docs(self, src_refer, fix_plugin):
        """Simple parser init with valid max_docs"""
        assert self.MyParser(src_refer, fix_plugin, 5, max_docs=2)

    def test_init_with_null_max_docs(self, src_refer, fix_plugin):
        """
        Simple parser init with zero value max_docs.
        Max_documents must be positive integer or None value.
        """
        try:
            self.MyParser(src_refer, fix_plugin, 5, max_docs=0)
        except AssertionError as e:
            assert True, e
        else:
            assert False, "max_documents must be positive integer or None value"

    def test_content_without_limits(self, src_refer, fix_plugin):
        mp = self.MyParser(src_refer, fix_plugin, 5)
        _out: tuple[S3PDocument, ...] | None = None
        try:
            _out = mp.content()
        except Exception as e:
            assert False, f"{e}"
        else:
            assert len(_out) == 5, "length of the plugin content result must be equal to 5"
            # assert True

    def test_content_when_result_len_is_greater_then_limit(self, src_refer, fix_plugin):
        mp = self.MyParser(src_refer, fix_plugin, 5, max_docs=3)
        _out: tuple[S3PDocument, ...] | None = None
        try:
            _out = mp.content()
        except Exception as e:
            assert False, f"{e}"
        else:
            assert len(_out) == 3, "length of the plugin content result must be equal to 5"

    def test_content_when_result_len_is_less_then_limit(self, src_refer, fix_plugin):
        mp = self.MyParser(src_refer, fix_plugin, 5, max_docs=7)
        _out: tuple[S3PDocument, ...] | None = None
        try:
            _out = mp.content()
        except Exception as e:
            assert False, f"{e}"
        else:
            assert len(_out) == 5, "length of the plugin content result must be equal to 5"
            # assert True

    def test_content_with_some_error(self, src_refer, fix_plugin):
        mp = self.MyParser(src_refer, fix_plugin, 5, max_docs=7, with_error=True)
        _out: tuple[S3PDocument, ...] | None = None
        try:
            _out = mp.content()
        except S3PPluginPayloadError as e:
            assert True, f"{e}"
        except Exception as e:
            assert False, f"{e}"
        else:
            assert False, "Parser stopped with an error"

    def test_content_with_last_docs_exist(self, src_refer, fix_plugin):
        _last_doc = random_doc()
        mp = self.MyParser(src_refer, fix_plugin, 5, max_docs=7, with_last_doc=_last_doc, last_doc=_last_doc)
        _out: tuple[S3PDocument, ...] | None = None
        try:
            _out = mp.content()
        except Exception as e:
            assert False, f"{e}"
        else:
            print(*_out, sep="\n")
            assert _last_doc not in _out, f"The last doc must be {_last_doc}"
            # assert False, "Parser stopped with an error"
