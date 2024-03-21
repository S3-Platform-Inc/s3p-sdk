import logging

from s3p_sdk.plugin.payloads.abc_payload_base import AbcS3PPayloadBase
from s3p_sdk.types import S3PRefer


class S3PPayloadBase(AbcS3PPayloadBase):

    def __init__(self, refer: S3PRefer, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        self._refer: S3PRefer = refer

        # Logging for payloads
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug(f"Payload class init completed")
        self.logger.info(f"Set "+self._refer.to_logging)
