"""Base source payload module"""
from s3p_sdk.exceptions.parser import S3PPluginPayloadError, S3PPluginParserFinish
from s3p_sdk.plugin.payloads.parsers.abc_parser_base import AbcS3PParserExtends
from s3p_sdk.plugin.payloads.payload_base import S3PPayloadBase
from s3p_sdk.types import S3PDocument, S3PRefer, S3PPlugin


class S3PParserBase(S3PPayloadBase, AbcS3PParserExtends):
    """
    Base class for payload of the source plugin
    """

    def __init__(self, refer: S3PRefer, plugin: S3PPlugin, max_documents: int = None, last_document: S3PDocument = None):
        assert max_documents is None or (isinstance(max_documents, int) and max_documents > 0), \
            "max_documents must be positive integer or None value"
        super().__init__(refer, plugin)
        self._parsed_document = []
        self._max_documents = max_documents
        self._last_document = last_document

    def content(self) -> tuple[S3PDocument, ...]:
        self.logger.debug("Parse process start")
        try:
            self._parse()
        except S3PPluginParserFinish as e:
            self.logger.debug(str(e))
        except Exception as e:
            er = S3PPluginPayloadError(self._plugin, "Parsing stopped with error", e)
            self.logger.error(str(er))
            raise er from e
        else:
            self.logger.debug("Parse process finished")
        return tuple(self._parsed_document)

    def _parse(self) -> None:
        pass

    def _find(self, document: S3PDocument):
        """
        A method of checking that the number of documents has exceeded the maximum number or the found document is
        equal to the last document
        """
        if self._last_document is not None and self._last_document.hash == document.hash:
            raise S3PPluginParserFinish(self._plugin, f"Find already existing document ({self._last_document.to_logging})")

        if self._max_documents is not None and len(self._parsed_document) >= self._max_documents:
            raise S3PPluginParserFinish(self._plugin, f"Max count articles reached ({self._max_documents})")

        self._parsed_document.append(document)
        self.logger.info(f'Find '+document.to_logging)
