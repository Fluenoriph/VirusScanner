import abc
from modules.real_time import CurrentTime


class BaseAnalyser(abc.ABC):
    API_URL = 'https://www.virustotal.com/api/v3/'

    def __init__(self, api_key, endpoint, data):
        self.headers = { 'x-apikey': api_key }
        self.endpoint = endpoint
        self.data = data

    @abc.abstractmethod
    def analyse(self):
        pass

    #def response_correcting(self):
