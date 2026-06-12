import os
from modules.target_data_parser.base_directory_parser import BaseDirectoryParser


class FileVariantDirectoryParser(BaseDirectoryParser):
    def __init__(self, path):
        super().__init__(path)

    def parse(self):
        with os.scandir(self.path) as entries:
            for entry in entries:
                if entry.is_file(follow_symlinks=False):
                    self.parsed_data.append(entry.path)