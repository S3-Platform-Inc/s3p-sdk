import pytest

from s3p_sdk.types import S3PRefer
from s3p_sdk.plugin.types import SOURCE, ML


def refers(_type: str) -> S3PRefer:
    """

    :param _type:
    :return:
    """
    return {
            SOURCE: S3PRefer(1, "test ref 1", SOURCE, None),
            ML: S3PRefer(2, "test ref 2", ML, None),
        }.get(_type)


@pytest.fixture
def src_refer() -> S3PRefer:
    """

    :return:
    """
    return refers(SOURCE)
