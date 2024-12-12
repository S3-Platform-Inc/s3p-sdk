from dataclasses import dataclass


@dataclass
class Manifest:
    """The presentation of plugin.xml file"""
    version: str
    plugin_name: str
