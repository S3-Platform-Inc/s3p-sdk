import json

import pytest
from datetime import datetime
from s3p_sdk.plugin.config import RestrictionsConfig


@pytest.mark.config_set
class TestRestrictionsConfig:
    def test_initialization(self):
        config = RestrictionsConfig(
            maximum_materials=10,
            to_last_material=True,
            from_date=datetime(2023, 1, 1),
            to_date=datetime(2023, 12, 31)
        )
        assert config.maximum_materials == 10
        assert config.to_last_material is True
        assert config.from_date == datetime(2023, 1, 1)
        assert config.to_date == datetime(2023, 12, 31)

    def test_dict_method(self):
        config = RestrictionsConfig(
            maximum_materials=5,
            to_last_material=False,
            from_date=datetime(2023, 6, 1),
            to_date=datetime(2023, 6, 30)
        )
        expected_dict = {
            "max_materials": 5,
            "last_material": False,
            "from_date": datetime(2023, 6, 1).isoformat(),
            "to_date": datetime(2023, 6, 30).isoformat(),
        }
        assert config.dict() == expected_dict

    def test_none_values(self):
        config = RestrictionsConfig(
            maximum_materials=None,
            to_last_material=None,
            from_date=None,
            to_date=None
        )
        assert config.maximum_materials is None
        assert config.to_last_material is None
        assert config.from_date is None
        assert config.to_date is None
        expected_dict = {
            "max_materials": None,
            "last_material": None,
            "from_date": None,
            "to_date": None,
        }
        assert config.dict() == expected_dict

    def test_mixed_values(self):
        config = RestrictionsConfig(
            maximum_materials=3,
            to_last_material=True,
            from_date=None,
            to_date=datetime(2023, 12, 31)
        )
        assert config.maximum_materials == 3
        assert config.to_last_material is True
        assert config.from_date is None
        assert config.to_date == datetime(2023, 12, 31)
        expected_dict = {
            "max_materials": 3,
            "last_material": True,
            "from_date": None,
            "to_date": datetime(2023, 12, 31).isoformat(),
        }
        assert config.dict() == expected_dict

    def test_save_to_json(self):
        config = RestrictionsConfig(
            maximum_materials=3,
            to_last_material=True,
            from_date=None,
            to_date=datetime(2023, 12, 31)
        )

        print(config.dict())
        js_string = json.dumps(config.dict())
        loaded_json = json.loads(js_string)
        print(js_string)
        print(loaded_json)
        assert datetime(2023, 12, 31) == datetime.fromisoformat(loaded_json.get("to_date"))

