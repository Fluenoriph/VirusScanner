from enum import Enum


class ProcessCode(Enum):
    SCANNING_COMPLETED = '> Scanning process successful <'
    SCANNING_FAILED = '> Scanning process error <'
    TARGET_DATA_ERROR = '> Bad argument <'
    FILE_NOT_FOUND = '> File not found <'
    FILE_TOO_LARGE = '> File too large <'