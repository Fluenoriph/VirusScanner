# 'base_directory_parser.py' - базовый класс для парсеров данных из директории (папки).

from abc import ABC, abstractmethod


class BaseDirectoryParser(ABC):
    def __init__(self, path):
        self.path = path
        self._parsed_data = []

    @property
    def parsed_data(self):
        return self._parsed_data

    @abstractmethod
    def parse(self):
        pass
