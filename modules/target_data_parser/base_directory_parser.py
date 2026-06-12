import abc


class BaseDirectoryParser(abc.ABC):
    def __init__(self, path):
        self.path = path
        self._parsed_data = []

    @property
    def parsed_data(self):
        return self._parsed_data

    @abc.abstractmethod
    def parse(self):
        pass