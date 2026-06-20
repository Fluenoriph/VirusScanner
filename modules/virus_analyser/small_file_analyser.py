import requests
from modules.app_data import AppData
from modules.virus_analyser.base_analyser import BaseAnalyser
from modules.virus_analyser.analyses_endpoint_analyser import AnalysesEndpointAnalyser


class SmallFileAnalyser(AnalysesEndpointAnalyser):
    def __init__(self, api_key, data_for_analysis, target_type = AppData.TARGET[3]):
        super().__init__(api_key, data_for_analysis, target_type)

    def add_analysed_data_info(self, response_json):
        self.result_data.update({ 'sha256': response_json['meta']['file_info']['sha256']})
        self.result_data.update({ 'size': response_json['meta']['file_info']['size']})

    def get_data_id(self):
        with open(self.data_for_analysis, 'rb') as file:
            files = { self.target_type: (self.data_for_analysis, file)}

            return requests.post(BaseAnalyser.API_URL + AppData.ENDPOINT[self.target_type]['small'],
                                 headers=self.headers, files=files)


