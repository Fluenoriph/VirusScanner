import os
from modules.program_process.process_code import ProcessCode
from modules.virus_analyser.big_file_analyser import BigFileAnalyser
from modules.virus_analyser.small_file_analyser import SmallFileAnalyser


class FileAnalyserSelector:
    # bytes
    SMALL_FILE_SIZE_THRESHOLD = 33554432
    BIG_FILE_SIZE_THRESHOLD = 209715200

    @staticmethod
    def select(file):
        try:
            size = os.path.getsize(file)
        except OSError:
            return ProcessCode.FILE_NOT_FOUND
        else:
            if size < FileAnalyserSelector.SMALL_FILE_SIZE_THRESHOLD:
                return SmallFileAnalyser()
            elif size < FileAnalyserSelector.BIG_FILE_SIZE_THRESHOLD:
                return BigFileAnalyser()
            else:
                return ProcessCode.FILE_TOO_LARGE
