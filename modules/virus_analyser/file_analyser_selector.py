import os
from modules.program_process.program_codes import ProcessCode
from modules.virus_analyser.big_file_analyser import BigFileAnalyser
from modules.virus_analyser.small_file_analyser import SmallFileAnalyser


class FileAnalyserSelector:
    # bytes
    SMALL_FILE_SIZE_THRESHOLD = 33554432
    BIG_FILE_SIZE_THRESHOLD = 209715200

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

        if size < FileAnalyserSelector.SMALL_FILE_SIZE_THRESHOLD:
            self.analyser = SmallFileAnalyser()
            self.analyser.data_for_analysis = file

            return True
        elif size < FileAnalyserSelector.BIG_FILE_SIZE_THRESHOLD:
            self.analyser = BigFileAnalyser()
            self.analyser.data_for_analysis = file

            return True
        else:
            return False
