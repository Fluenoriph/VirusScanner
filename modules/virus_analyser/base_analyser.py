import abc
import requests
from modules.app_data import AppData
from modules.real_time import CurrentTime


class BaseAnalyser(abc.ABC):
    API_URL = 'https://www.virustotal.com/api/v3/'
    SUCCESSFUL_CODE = 200

    def __init__(self, target_type):
        self.target_type = target_type
        self._api_key = None
        self._data_for_analysis = None

        self.headers = { 'x-apikey': self.api_key}
        self.standard_request_get = lambda endpoint: requests.get(BaseAnalyser.API_URL + endpoint, headers=self.headers)
        self.add_time = lambda: self.result_data.update({ 'analysis time': CurrentTime.get_time() })
        self.add_stats = lambda response_json: self.result_data.update(response_json['data']['attributes']
                                                                  [AppData.STATS_KEY[self.target_type]])

        self._result_data = {}
    
    @property
    def api_key(self):
        return self._api_key
    
    @api_key.setter
    def api_key(self, value):
        self._api_key = value

    @property
    def data_for_analysis(self):
        return self._data_for_analysis

    @data_for_analysis.setter
    def data_for_analysis(self, value):
        self._data_for_analysis = value
    
    @property
    def result_data(self):
        return self._result_data

    @abc.abstractmethod
    def analyse(self):
        pass

    @abc.abstractmethod
    def add_analysed_data_info(self, response):
        pass
