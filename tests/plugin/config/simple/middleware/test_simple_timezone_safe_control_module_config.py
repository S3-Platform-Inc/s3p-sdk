import datetime

from s3p_sdk.plugin.config.modules import AbcModuleConfig, TimezoneSafeControlConfig, \
    CutJunkCharactersFromDocumentTextConfig


class TestSimpleTimezoneSafeControlModuleConfig:

    def test_minimal_init(self):
        test_module: AbcModuleConfig = TimezoneSafeControlConfig(
            order=1,
            is_critical=True,
        )
        assert test_module
        assert test_module.dict()

    def test_maximal_init(self):
        test_module: AbcModuleConfig = TimezoneSafeControlConfig(
            order=1,
            is_critical=True,
            p_fields=['published', ]
        )
        assert test_module
        assert test_module.dict()

    def test_order_check(self):
        try:
            test_module: AbcModuleConfig = TimezoneSafeControlConfig(
                order=None,
                is_critical=True,
            )
        except AssertionError:
            assert True

    def test_simple_generate_config_with_one_field(self):
        test_module: AbcModuleConfig = TimezoneSafeControlConfig(
            order=1,
            is_critical=True,
            p_fields=['loaded', ]
        )
        test_dict = test_module.dict()
        schema_dict = {
            "order": 1,
            "name": 'TimezoneSafeControl',
            'critical': True,
            'params': {
                "fields": [
                    'loaded'
                ]
            }
        }
        print(test_dict)
        print(schema_dict)

        assert test_dict == schema_dict

    def test_simple_generate_config_without_field(self):
        test_module: AbcModuleConfig = TimezoneSafeControlConfig(
            order=1,
            is_critical=True,
        )
        test_dict = test_module.dict()
        schema_dict = {
            "order": 1,
            "name": 'TimezoneSafeControl',
            'critical': True,
            'params': {}
        }
        print(test_dict)
        print(schema_dict)

        assert test_dict == schema_dict

    def test_simple_generate_config_with_false_critical(self):
        test_module: AbcModuleConfig = TimezoneSafeControlConfig(
            order=1,
            is_critical=False,
        )
        test_dict = test_module.dict()
        schema_dict = {
            "order": 1,
            "name": 'TimezoneSafeControl',
            'critical': False,
            'params': {}
        }
        print(test_dict)
        print(schema_dict)

        assert test_dict == schema_dict
