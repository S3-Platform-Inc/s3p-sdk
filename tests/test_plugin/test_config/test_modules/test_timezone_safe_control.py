import pytest

from s3p_sdk.plugin.config.modules import TimezoneSafeControlConfig


@pytest.mark.config_set
class TestTimezoneSafeConfig:

    def test_init(self):
        order = 1
        name = "TimezoneSafeControl"
        is_critical = False
        parameters = ["published", "loaded"]

        m = TimezoneSafeControlConfig(order, is_critical, parameters)

        assert m.dict() == {
            'order': order,
            'name': name,
            'critical': is_critical,
            'params': {
                'fields': parameters,
            }
        }

    def test_null_parameters(self):
        order = 1
        name = "TimezoneSafeControl"
        is_critical = False

        m = TimezoneSafeControlConfig(order, is_critical)

        assert m.dict() == {
            'order': order,
            'name': name,
            'critical': is_critical,
            'params': {}
        }

    def test_not_order(self):
        is_critical = False

        try:
            TimezoneSafeControlConfig(is_critical)
        except AssertionError:
            assert True

    def test_mistake_parameters(self):
        order = 1
        is_critical = False
        try:
            TimezoneSafeControlConfig(order, is_critical, ["text",])
        except AssertionError as e:
            assert True


