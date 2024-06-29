from abc import ABC, abstractmethod


class AbcObject(ABC):
    """
    Abstract class of the configuration object of s3p plugin
    """

    @abstractmethod
    def dict(self) -> dict:
        """
        :return: Dictionary of the configuration object
        """
        ...
