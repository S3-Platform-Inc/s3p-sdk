import pytest

from s3p_sdk.types import S3PRefer, S3PPlugin
from s3p_sdk.plugin.types import SOURCE, ML


@pytest.fixture
def fix_plugin() -> S3PPlugin:
    """

    :return:
    """
    return S3PPlugin(None, "unittest/test-rep-1", True, None, None, SOURCE, None)
