from s3p_sdk.plugin.config import CoreConfig
from s3p_sdk.plugin.types import SOURCE


class TestSimpleCoreConfig:

    def test_init(self):
        test_plugin = CoreConfig(
            reference='ieee',
            type=SOURCE,
            files=['ieee.py', ],
            is_localstorage=False
        )
        print(test_plugin)
        print(test_plugin.dict())
        assert test_plugin

    def test_simple_generate_config(self):
        test_plugin = CoreConfig(
            reference='ieee',
            type=SOURCE,
            files=['ieee.py', ],
            is_localstorage=False
        )
        test_dict = test_plugin.dict()
        schema_dict = {
            "reference": "ieee",
            "type": "SOURCE",
            "filenames": ["ieee.py"],
            "localstorage": False
        }
        print(test_dict)
        print(schema_dict)

        assert test_dict == schema_dict
