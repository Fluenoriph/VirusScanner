import os
from unittest import result

from modules.program_process.process_code import ProcessCode
from modules.virus_analyser.big_file_analyser import BigFileAnalyser
from modules.virus_analyser.small_file_analyser import SmallFileAnalyser


class FileAnalyserSelector:
    # bytes
    SMALL_FILE_SIZE_THRESHOLD = 33554432
    BIG_FILE_SIZE_THRESHOLD = 209715200

    def __init__(self):
        self._result = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def select(self, file):
        try:
            size = os.path.getsize(file)
        except OSError:
            self.result = ProcessCode.FILE_NOT_FOUND

            return False
        else:
            if size < FileAnalyserSelector.SMALL_FILE_SIZE_THRESHOLD:
                self.result = SmallFileAnalyser()
                self.result.data_for_analysis = file

                return True
            elif size < FileAnalyserSelector.BIG_FILE_SIZE_THRESHOLD:
                self.result = BigFileAnalyser()
                self.result.data_for_analysis = file

                return True
            else:
                self.result = ProcessCode.FILE_TOO_LARGE

                return False
