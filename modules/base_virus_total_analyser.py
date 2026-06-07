import abc
from modules.real_time import CurrentTime


class BaseVirusTotalAnalyser(abc.ABC):
    API_URL = 'https://www.virustotal.com/api/v3/'
    #ANALYSIS_STATUS = ("malicious", "suspicious", "undetected", "harmless")

    def __init__(self, api_key):
        self.headers = { 'x-apikey': api_key }

    @abc.abstractmethod
    def analyze(self, endpoint, data):
        pass
