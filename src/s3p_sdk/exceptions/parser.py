from s3p_sdk.types import S3PPlugin, S3PDocument


class S3PPluginPayloadError(Exception):
    """Error raised when the plugin stopped working with some problems"""

    def __init__(self, plugin: S3PPlugin, message, errors=None):
        self.plugin = plugin
        self.errors = errors
        self.message = message
        super().__init__(self._message())

    def _message(self) -> str:
        return f"""
        Plugin {self.plugin.repository} 
        stopped working with errors: {self.errors}.
        description: {self.message}.
        """

    def __repr__(self):
        return self._message()


class S3PPluginParserFinish(Exception):
    """Error raised when the plugin stopped because found necessary materials"""

    def __init__(self, plugin: S3PPlugin, message, errors=None):
        self.plugin = plugin
        self.errors = errors
        self.message = message
        super().__init__(self._message())

    def _message(self) -> str:
        return f"""
        Plugin {self.plugin.repository} 
        stopped working
        description: {self.message}.
        """

    def __repr__(self):
        return self._message()


class S3PPluginParserOutOfRestrictionException(Exception):
    """Error raised when found material is out of plugin restrictions"""

    def __init__(self, plugin: S3PPlugin, material: S3PDocument, restriction: str, errors=None):
        self.plugin = plugin
        self.material = material
        self.restriction = restriction
        self.errors = errors
        super().__init__(self._message())

    def _message(self) -> str:
        return f"""
        Plugin {self.plugin.repository} 
        found material: {self.material}
        that out of restriction: {self.restriction}.
        """

    def __repr__(self):
        return self._message()


class S3PPluginParserDocumentsAlreadyBeenFound(Exception):
    """Error raised when found material is already been found"""

    def __init__(self, plugin: S3PPlugin, document: S3PDocument, errors=None):
        self.plugin = plugin
        self.document = document
        self.errors = errors

    def _message(self) -> str:
        return f"""
        Plugin {self.plugin.repository}
        has already found document: {self.document}
        """
