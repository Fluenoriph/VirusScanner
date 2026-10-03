# 'small_file_analyser.py' - анализатор файлов менее 32 Мб.

import requests
import os
from modules.app_data import TARGET_FLAG, ENDPOINT, TARGET_NAME, API_URL
from modules.virus_analyser.base_analyser import BaseAnalyser
from modules.virus_analyser.analyses_endpoint_analyser import AnalysesEndpointAnalyser


class SmallFileAnalyser(AnalysesEndpointAnalyser):
    def __init__(self, target_flag = TARGET_FLAG[3]):
        super().__init__(target_flag)

    def add_analysed_data_info(self, response):
        self.result_data.update({ 'file': os.path.split(self.data_for_analysis)[1] })
        self.result_data.update({ 'sha256': response['meta']['file_info']['sha256'] })
        self.result_data.update({ 'size': response['meta']['file_info']['size'] })

    def get_analysed_data_id(self):
        with open(self.data_for_analysis, 'rb') as file:
            files = {TARGET_NAME[self.target_flag]: (self.data_for_analysis, file)}

            response = requests.post(API_URL + ENDPOINT[self.target_flag][0],
                                     headers={ 'x-apikey': self.api_key }, files=files)

            return BaseAnalyser.check_response_status(response)
