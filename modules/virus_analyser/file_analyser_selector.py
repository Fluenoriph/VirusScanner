# 'file_analyser_selector.py' - класс для выбора сущности анализатора файла в зависимости от его размера.

import os
from modules.virus_analyser.large_file_analyser import LargeFileAnalyser
from modules.virus_analyser.small_file_analyser import SmallFileAnalyser
from modules.app_data import SMALL_FILE_SIZE_THRESHOLD, LARGE_FILE_SIZE_THRESHOLD


class FileAnalyserSelector:
    def __init__(self):
        self._analyser = None

    @property
    def analyser(self):
        return self._analyser

    @analyser.setter
    def analyser(self, value):
        self._analyser = value

    def select(self, file):
        size = os.path.getsize(file)

        if size < SMALL_FILE_SIZE_THRESHOLD:
            self.analyser = SmallFileAnalyser()
            self.analyser.data_for_analysis = file

            return True

        elif size < LARGE_FILE_SIZE_THRESHOLD:
            self.analyser = LargeFileAnalyser()
            self.analyser.data_for_analysis = file

            return True

        else:
            return False
