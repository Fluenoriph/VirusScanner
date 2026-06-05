import re
from modules.base_data_file_parser import BaseDataFileParser


class URLDataFileParser(BaseDataFileParser):
    def __init__(self, data_file):
        super().__init__(data_file)

    @staticmethod
    def get_regex_pattern():
        return re.compile(r'')