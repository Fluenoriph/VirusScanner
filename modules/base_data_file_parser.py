import abc
import re


class BaseDataFileParser(abc.ABC):
    def __init__(self, data_file):
        self.data_file = data_file
        self._matched_data = []

    @property
    def matched_data(self):
        return self._matched_data

    @staticmethod
    @abc.abstractmethod
    def get_regex_pattern():
        pass

    def parse(self):
        with open(self.data_file, 'r') as file:
            data = file.readlines()

            for line in data:
                match = re.search(self.get_regex_pattern(), line)

                if match:
                    self.matched_data.append(match.group())