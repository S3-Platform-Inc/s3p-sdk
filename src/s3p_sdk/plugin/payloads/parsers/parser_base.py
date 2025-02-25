"""Base source payload module"""
from s3p_sdk.exceptions.parser import S3PPluginPayloadError, S3PPluginParserFinish, \
    S3PPluginParserOutOfRestrictionException
from s3p_sdk.plugin.payloads.parsers.abc_parser_base import AbcS3PParserExtends
from s3p_sdk.plugin.payloads.payload_base import S3PPayloadBase
from s3p_sdk.types import S3PDocument, S3PRefer, S3PPlugin, S3PPluginRestrictions
from s3p_sdk.types.plugin_restrictions import FROM_DATE, TO_DATE


class S3PParserBase(S3PPayloadBase, AbcS3PParserExtends):
    """
    Base class for payload of the source plugin
    """

    def __init__(self, refer: S3PRefer, plugin: S3PPlugin, restrictions: S3PPluginRestrictions):
        assert restrictions.maximum_materials is None or (isinstance(restrictions.maximum_materials, int) and restrictions.maximum_materials > 0), \
            "max_documents must be positive integer or None value"
        super().__init__(refer, plugin)
        self._parsed_document = []
        self._restriction = restrictions

    def content(self) -> tuple[S3PDocument, ...]:
        self.logger.debug("Parse process start")
        try:
            self._parse()
        except S3PPluginParserFinish as e:
            self.logger.debug(str(e))
        except Exception as e:
            er = S3PPluginPayloadError(self._plugin, f"Parsing stopped with error: {e}", e)
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
        equal to the last document.

        Also, this method checks date restrictions and determines if the current document is the last required one.

        Note for developers:
        This method may raise S3PPluginParserOutOfRestrictionException when a document's publication date
        is outside the specified date range (from_date or to_date). It's recommended to wrap calls to this
        method in a try-except block and handle these exceptions appropriately in your _parse method.
        This will prevent the parser from stopping prematurely when encountering documents outside the date range.

        Example:
        def _parse(self):
            for document in self.get_documents():
                try:
                    self._find(document)
                except S3PPluginParserOutOfRestrictionException:
                    self.logger.warning(f"Document {document.id} is outside the specified date range")
                except S3PPluginParserFinish as e:
                    raise e

        :param document: The document to be checked and potentially added to _parsed_document
        :raises S3PPluginParserOutOfRestrictionException: If the document is outside the specified date range
        :raises S3PPluginParserFinish: If the maximum number of documents is reached or the last document is found
        """

        if self._restriction.from_date is not None and document.published < self._restriction.from_date:
            raise S3PPluginParserOutOfRestrictionException(self._plugin, document, FROM_DATE)

        if self._restriction.to_date is not None and document.published > self._restriction.to_date:
            raise S3PPluginParserOutOfRestrictionException(self._plugin, document, TO_DATE)

        if self._restriction.to_last_material is not None and self._restriction.to_last_material.hash == document.hash:
            raise S3PPluginParserFinish(self._plugin, f"Find already existing document ({self._restriction.to_last_material.to_logging})")

        is_last_required = False
        if self._restriction.maximum_materials is not None:
            if len(self._parsed_document) >= self._restriction.maximum_materials:
                raise S3PPluginParserFinish(self._plugin, f"Max count articles reached ({self._restriction.maximum_materials})")
            elif len(self._parsed_document) == self._restriction.maximum_materials - 1:
                is_last_required = True

        self._parsed_document.append(document)
        self.logger.info(f'Find ' + document.to_logging)

        if is_last_required:
            raise S3PPluginParserFinish(self._plugin,
                                        f"Last required document added ({self._restriction.maximum_materials})")
