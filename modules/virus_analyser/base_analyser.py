import abc
import requests

from modules.app_data import AppData
from modules.real_time import CurrentTime


class BaseAnalyser(abc.ABC):
    API_URL = 'https://www.virustotal.com/api/v3/'
    SUCCESSFUL_CODE = 200

    def __init__(self, api_key, data_for_analysis, target_type):
        self.headers = { 'x-apikey': api_key }
        self.data_for_analysis = data_for_analysis
        self.target_type = target_type

        self.standard_request_get = lambda endpoint: requests.get(BaseAnalyser.API_URL + endpoint, headers=self.headers)
        self.add_time = lambda: self.result_data.update({ 'analysis time': CurrentTime.get_time() })
        self.add_stats = lambda response_json: self.result_data.update(response_json['data']['attributes']
                                                                  [AppData.STATS_KEY[self.target_type]])

        self._result_data = {}

    @property
    def result_data(self):
        return self._result_data

    @abc.abstractmethod
    def analyse(self):
        pass

    @abc.abstractmethod
    def add_analysed_data_info(self, response):
        pass
