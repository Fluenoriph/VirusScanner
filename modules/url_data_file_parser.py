import re
from modules.base_data_file_parser import BaseDataFileParser


class URLDataFileParser(BaseDataFileParser):
    def __init__(self, data_file):
        super().__init__(data_file)

    @staticmethod
    def get_regex_pattern():
        return re.compile(r"^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\."
                          r"[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$")  # without domens test !