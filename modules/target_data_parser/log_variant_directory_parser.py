import os
from modules.target_data_parser.base_directory_parser import BaseDirectoryParser


class LogVariantDirectoryParser(BaseDirectoryParser):
    def __init__(self, path):
        super().__init__(path)

    def parse(self):
        with os.scandir(self.path) as entries:
            for entry in entries:
                if entry.is_file(follow_symlinks=False) and (entry.name.endswith(".txt")
                                                             or entry.name.endswith(".log")):
                    self.parsed_data.append(entry.path)
