from s3p_sdk.types import S3PPlugin


class S3PPluginPayloadError(Exception):
    """Error raised when the plugin stopped working with some problems"""

    def __init__(self, plugin: S3PPlugin, message, errors=None):
        super().__init__(message)
        self.plugin = plugin
        self.errors = errors
        self.message = message

    def __repr__(self):
        # Display the errors
        # print('Plugin {}')
        # print(self.errors)
        return f"""
        Plugin {self.plugin.repository} 
        stopped working with errors: {self.errors}.
        description: {self.message}.
        """


class S3PPluginParserFinish(Exception):
    """Error raised when the plugin stopped because found necessary materials"""

    def __init__(self, plugin: S3PPlugin, message, errors=None):
        super().__init__(message)
        self.plugin = plugin
        self.errors = errors
        self.message = message

    def __repr__(self):
        # Display the errors
        # print('Plugin {}')
        # print(self.errors)
        return f"""
        Plugin {self.plugin.repository} 
        stopped working
        description: {self.message}.
        """
