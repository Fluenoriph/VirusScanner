# 'base_analyser.py' - базовый класс для анализаторов данных посредством интеграции с Virus Total API v3.

from abc import ABC, abstractmethod
import requests
from rich import print
from modules.app_data import STATS_KEY, API_URL, FAILURE_COLOR
from modules.real_time import get_current_time
from modules.program_logger import logging
from modules.program_codes import CODE_20, CODE_21, CODE_200


class BaseAnalyser(ABC):
    def __init__(self, target_flag):
        self.target_flag = target_flag
        self._api_key = None
        self._data_for_analysis = None
        self._result_data = {}

        self.add_current_time = lambda: self.result_data.update({'analysis time': get_current_time()})

        self.add_stats = lambda response_json: self.result_data.update(response_json['data']['attributes']
                                                           [STATS_KEY[self.target_flag]])

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

    @abstractmethod
    def analyse(self):
        pass

    @abstractmethod
    def add_analysed_data_info(self, response):
        pass

    @staticmethod
    def check_response_status(response):
        if response.status_code == CODE_200:
            return response.json()
        else:
            logging.error(f'{CODE_21}: {response.status_code}')
            print(f'\n[{FAILURE_COLOR}]> {CODE_21} ![/{FAILURE_COLOR}]')

            return None

    # Иногда, по неизвестным причинам, все счетчики возвращают нули в ответе, чего по логике не должно быть,
    # поэтому делается проверка и повторяется запрос несколько раз, до должного ответа.
    def check_null_status_values(self, response_json):
        stats = response_json['data']['attributes'][STATS_KEY[self.target_flag]]

        virus_engines_test_count = 0
        for value in stats.values():
            virus_engines_test_count += value

        if virus_engines_test_count != 0:
            return True
        else:
            logging.warning(CODE_20)

            return False

    def get_standard_request(self, endpoint):
        response = requests.get(API_URL + endpoint, headers={ 'x-apikey': self.api_key })

        return BaseAnalyser.check_response_status(response)
