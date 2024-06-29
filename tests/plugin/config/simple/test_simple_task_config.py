import datetime

from s3p_sdk.plugin.config import TaskConfig, trigger


class TestSimpleTaskConfig:

    def test_init(self):
        test_task = TaskConfig(
            trigger=trigger.TriggerConfig(
                type=trigger.SCHEDULE,
                interval=datetime.timedelta(days=7),
            )
        )
        assert test_task
        assert test_task.dict()

    def test_simple_generate_config_with_big_interval(self):
        test_task = TaskConfig(
            trigger=trigger.TriggerConfig(
                type=trigger.SCHEDULE,
                interval=datetime.timedelta(days=7),
            )
        )
        test_dict = test_task.dict()
        schema_dict = {
            "trigger": {
                "type": 'SCHEDULE',
                "interval": f'{7*24*60*60} seconds'
            }
        }
        print(test_dict)
        print(schema_dict)

        assert test_dict == schema_dict

    def test_simple_generate_config_with_small_interval(self):
        test_task = TaskConfig(
            trigger=trigger.TriggerConfig(
                type=trigger.SCHEDULE,
                interval=datetime.timedelta(hours=6),
            )
        )
        test_dict = test_task.dict()
        schema_dict = {
            "trigger": {
                "type": 'SCHEDULE',
                "interval": f'{6*60*60} seconds'
            }
        }
        print(test_dict)
        print(schema_dict)

        assert test_dict == schema_dict
