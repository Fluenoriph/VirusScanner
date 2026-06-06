import abc
from modules.real_time import CurrentTime


class BaseVirusTotalChecker(abc.ABC):
    API_URL = 'https://www.virustotal.com/api/v3/'
    ANALYSIS_STATUS = ("malicious", "suspicious", "undetected", "harmless")
    

