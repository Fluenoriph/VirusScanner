import os
from modules.virus_analyser.big_file_analyser import BigFileAnalyser
from modules.virus_analyser.small_file_analyser import SmallFileAnalyser
from modules.app_data import SMALL_FILE_SIZE_THRESHOLD, BIG_FILE_SIZE_THRESHOLD


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

        elif size < BIG_FILE_SIZE_THRESHOLD:
            self.analyser = BigFileAnalyser()
            self.analyser.data_for_analysis = file

            return True

        else:
            return False
