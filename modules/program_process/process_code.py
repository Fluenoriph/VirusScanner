from enum import Enum


class ProcessCode(Enum):
    SCANNING_COMPLETED = '> Scanning process successful <'
    SCANNING_FAILED = '> Scanning process error <'
    TARGET_DATA_ERROR = '> Bad argument <'