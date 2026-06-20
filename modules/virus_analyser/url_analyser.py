import requests
from modules.app_data import AppData
from modules.virus_analyser.analyses_endpoint_analyser import AnalysesEndpointAnalyser
from modules.virus_analyser.base_analyser import BaseAnalyser


class UrlAnalyser(AnalysesEndpointAnalyser):
    def __init__(self, api_key, data_for_analysis, target_type = AppData.TARGET[2]):
        super().__init__(api_key, data_for_analysis, target_type)

    def add_analysed_data_info(self, response_json):
        self.result_data.update( {self.target_type: response_json['meta']['url_info']['url']} )

    def get_data_id(self):
        return requests.post(BaseAnalyser.API_URL + AppData.ENDPOINT[self.target_type], headers=self.headers,
                             data={ self.target_type: self.data_for_analysis} )
