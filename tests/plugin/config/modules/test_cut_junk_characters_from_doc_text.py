from s3p_sdk.plugin.config.modules import CutJunkCharactersFromDocumentTextConfig


class TestCutJunkCharactersFromDocumentTextConfig:
    NAME = 'CutJunkCharactersFromDocumentText'

    def test_init(self):
        order = 1
        is_critical = False
        parameters = ["text", "title", "abstract"]

        m = CutJunkCharactersFromDocumentTextConfig(order, is_critical, parameters)

        assert m.dict() == {
            'order': order,
            'name': self.NAME,
            'critical': is_critical,
            'params': {
                'fields': parameters,
            }
        }

    def test_half_init(self):
        order = 1
        is_critical = False
        parameters = ["text",]

        m = CutJunkCharactersFromDocumentTextConfig(order, is_critical, parameters)

        assert m.dict() == {
            'order': order,
            'name': self.NAME,
            'critical': is_critical,
            'params': {
                'fields': parameters,
            }
        }

    def test_null_parameters(self):
        order = 1
        is_critical = False

        m = CutJunkCharactersFromDocumentTextConfig(order, is_critical)

        assert m.dict() == {
            'order': order,
            'name': self.NAME,
            'critical': is_critical,
            'params': {}
        }

    def test_not_order(self):
        is_critical = False

        try:
            CutJunkCharactersFromDocumentTextConfig(is_critical)
        except AssertionError:
            assert True

    def test_mistake_parameters(self):
        order = 1
        is_critical = False
        try:
            CutJunkCharactersFromDocumentTextConfig(order, is_critical, ["payload",])
        except AssertionError as e:
            assert True


