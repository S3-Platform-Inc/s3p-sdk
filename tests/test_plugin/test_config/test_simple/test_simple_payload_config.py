import pytest

from s3p_sdk.plugin.config import PayloadConfig
from s3p_sdk.plugin.config.payload import entry
from s3p_sdk.module import UndetectedWebdriver


@pytest.mark.config_set
class TestSimplePayloadConfig:

    def test_init(self): ...

    def test_payload_parameters(self): ...

    def test_payload_undetected_module_as_param(self):
        entry_param = entry.ModuleParamConfig('web_driver', UndetectedWebdriver, True)

        assert entry_param.dict() == {
            'key': 'web_driver',
            'value': {
                'type': 'module',
                'name': str(UndetectedWebdriver),
                'bus': True,
            }
        }
