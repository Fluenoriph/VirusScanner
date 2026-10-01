import abc
import requests
from rich import print
from modules.app_data import STATS_KEY, API_URL
from modules.real_time import CurrentTime
from modules.program_logger import ProgramLogger
from modules.program_codes import ProgramCodes as pc


class BaseAnalyser(abc.ABC):
    logger = ProgramLogger()

    def __init__(self, target_flag):
        self.target_flag = target_flag
        self._api_key = None
        self._data_for_analysis = None

        self.add_time = lambda: self.result_data.update({ 'analysis time': CurrentTime.get_current_time()})

        self.add_stats = lambda response_json: self.result_data.update(response_json['data']['attributes']
                                                                  [STATS_KEY[self.target_flag]])

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

    def check_bad_status_values(self, response_json):
        stats = response_json['data']['attributes'][STATS_KEY[self.target_flag]]

        virus_engines_test_count = 0
        for value in stats.values():
            virus_engines_test_count += value

        if virus_engines_test_count != 0:
            BaseAnalyser.logger.logger.error(pc.CODE_20)

            return True
        else:
            return False

    def get_standard_request(self, endpoint):
        response = requests.get(API_URL + endpoint, headers={ 'x-apikey': self.api_key })

        if response.status_code == pc.CODE_200:
            return response.json()
        else:
            BaseAnalyser.logger.logger.error(pc.CODE_21)
            print(f'[red]> {pc.CODE_21} ![/red]\n')

            return None
