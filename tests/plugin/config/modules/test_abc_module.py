from s3p_sdk.plugin.config.modules import AbcModuleConfig


class TestAbcModuleConfig:

    def _module(self, order, name, is_critical, parameters):
        """Init new TModule inherited from AbcModuleConfig"""

        class TModule(AbcModuleConfig):
            def __init__(self, o, n, i, p):
                self.order = o
                self.name = n
                self.is_critical = i
                self.parameters = p

        return TModule(order, name, is_critical, parameters)

    def test_generate_dict_normal(self):
        order = 1
        name = "name"
        is_critical = False
        parameters = {"a": 1, "b": 2}

        m = self._module(order, name, is_critical, parameters)

        assert m.dict() == {
            'order': order,
            'name': name,
            'critical': is_critical,
            'params': parameters if parameters else {},
        }
