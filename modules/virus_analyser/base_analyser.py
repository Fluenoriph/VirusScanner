import abc
from modules.real_time import CurrentTime


class BaseAnalyser(abc.ABC):
    API_URL = 'https://www.virustotal.com/api/v3/'
    STATS_KEY = 'last_analysis_stats'

    def __init__(self, api_key, endpoint, data):
        self.headers = { 'x-apikey': api_key }
        self.endpoint = endpoint
        self.data = data
        self._result_data = {}

    @property
    def result_data(self):
        return self._result_data

    @abc.abstractmethod
    def analyse(self):
        pass

    def add_analysis_stats(self, response_json, stats_key):
        self.result_data.update(response_json['data']['attributes'][stats_key])

    def check_response(self, response):
        if response.status_code == 200:
            self.result_data.update({ 'VirusTotal analysis time': CurrentTime.get_time() })

            return True
        else:
            return False
