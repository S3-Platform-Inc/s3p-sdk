"""Modules package"""
__all__ = [
    'AbcObject',
    'TaskConfig',
    'CoreConfig',
    'MiddlewareConfig',
    'PayloadConfig',
    'PluginConfig',
    'modules',
    'payload',
    'type',
    'trigger'
]

import dataclasses

from .abc_object import AbcObject
from .taskconfig import TaskConfig
from .coreconfig import CoreConfig
from .middlewareconfig import MiddlewareConfig
from .payload import PayloadConfig


@dataclasses.dataclass
class PluginConfig(AbcObject):
    """
    Main config dataclass
    """

    plugin: CoreConfig
    task: TaskConfig
    middleware: MiddlewareConfig
    payload: PayloadConfig

    def dict(self) -> dict:
        return {
            'plugin': self.plugin.dict(),
            'task': self.task.dict(),
            'middleware': self.middleware.dict(),
            'payload': self.payload.dict()
        }
