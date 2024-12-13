import pytest
import datetime

from s3p_sdk.plugin.config import (
    PluginConfig,
    CoreConfig,
    TaskConfig,
    trigger,
    MiddlewareConfig,
    modules,
    payload
)
from s3p_sdk.plugin.config.restrictconfig import RestrictionsConfig
from s3p_sdk.plugin.types import SOURCE
from s3p_sdk.module import (
    WebDriver,

)


class TestSimpleAllConfig:

    def test_simple_init(self):
        test_pc = PluginConfig(
            plugin=CoreConfig(
                reference='ieee',
                type=SOURCE,
                files=['ieee.py', ],
                is_localstorage=False,
                restrictions=RestrictionsConfig(
                    50, None, None, None
                )
            ),
            task=TaskConfig(
                trigger=trigger.TriggerConfig(
                    type=trigger.SCHEDULE,
                    interval=datetime.timedelta(days=7),
                )
            ),
            middleware=MiddlewareConfig(
                modules=[
                    modules.TimezoneSafeControlConfig(order=1, is_critical=True),
                    modules.CutJunkCharactersFromDocumentTextConfig(order=2, is_critical=True,
                                                                    p_fields=['text', 'abstract']),
                ],
                bus=None,
            ),
            payload=payload.PayloadConfig(
                file='ieee.py',
                classname='IEEE',
                entry=payload.entry.EntryConfig(
                    method='content',
                    params=[
                        payload.entry.ModuleParamConfig(key='driver', module_name=WebDriver, bus=True),
                        payload.entry.ConstParamConfig(key='url',
                                                       value='https://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=10005208&punumber=6287639&sortType=vol-only-newest'),
                        payload.entry.ConstParamConfig(key='categories', value=[
                            "Computational and artificial intelligence",
                            "Computers and information processing",
                            "Communications technology",
                            "Industry applications",
                            "Vehicular and wireless technologies",
                            "Systems engineering and theory",
                            "Intelligent transportation systems",
                            "Information theory",
                            "Electronic design automation and methodology",
                            "Education",
                            "Social implications of technology",
                        ])
                    ]
                )
            )
        )
        schema_pc = {
            "plugin": {
                "reference": "ieee",
                "type": "SOURCE",
                "filenames": ["ieee.py"],
                "localstorage": False,
                "restrictions": {
                    "mex_materials": 50,
                    "last_material": None,
                    "from_date": None,
                    "to_date": None,
                },
            },
            "task": {
                "trigger": {
                    "type": "SCHEDULE",
                    "interval": "604800 seconds"
                }
            },
            "middleware": {
                "modules": [
                    {"order": 1, "name": "TimezoneSafeControl", "critical": True, "params": {}},
                    {"order": 2, "name": "CutJunkCharactersFromDocumentText", "critical": True,
                     "params": {"fields": ["text", "abstract"]}}
                ]
            },
            "payload": {
                "file": "ieee.py",
                "class": "IEEE",
                "entry": {
                    "point": "content",
                    "params": [
                        {"key": "driver", "value": {"type": "module", "name": "WebDriver", "bus": True}},
                        {"key": "url", "value": {"type": "const",
                                                 "value": "https://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber"
                                                          "=10005208&punumber=6287639&sortType=vol-only-newest"}},
                        {"key": "categories", "value": {"type": "const", "value": [
                            "Computational and artificial intelligence",
                            "Computers and information processing",
                            "Communications technology",
                            "Industry applications",
                            "Vehicular and wireless technologies",
                            "Systems engineering and theory",
                            "Intelligent transportation systems",
                            "Information theory",
                            "Electronic design automation and methodology",
                            "Education",
                            "Social implications of technology"
                        ]}}
                    ]
                }
            }
        }

        print(test_pc.dict())
        print(schema_pc)
        assert test_pc.dict() == schema_pc

    def test_simple_generate_config(self):
        test_plugin = CoreConfig(
            reference='ieee',
            type=SOURCE,
            files=['ieee.py', ],
            is_localstorage=False,
            restrictions=RestrictionsConfig(None, None, None, None)
        )
        test_dict = test_plugin.dict()
        schema_dict = {
            "reference": "ieee",
            "type": "SOURCE",
            "filenames": ["ieee.py"],
            "localstorage": False,
            "restrictions": {
                "mex_materials": None,
                "last_material": None,
                "from_date": None,
                "to_date": None,
            },
        }
        print(test_dict)
        print(schema_dict)

        assert test_dict == schema_dict
