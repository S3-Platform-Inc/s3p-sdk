import logging

from s3p_sdk.plugin.payloads.abc_payload_base import AbcS3PPayloadBase
from s3p_sdk.types import S3PRefer, S3PPlugin


class S3PPayloadBase(AbcS3PPayloadBase):

    def __init__(self, refer: S3PRefer, plugin: S3PPlugin, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        self._refer: S3PRefer = refer
        self._plugin: S3PPlugin = plugin

        # Logging for payloads
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug(f"Payload class init completed")
        self.logger.info(f"Set "+self._refer.to_logging)
