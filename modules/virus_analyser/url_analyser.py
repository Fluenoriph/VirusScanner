import requests
from modules.app_data import TARGET_FLAG, ENDPOINT, TARGET_NAME
from modules.virus_analyser.analyses_endpoint_analyser import AnalysesEndpointAnalyser
from modules.virus_analyser.base_analyser import BaseAnalyser


class UrlAnalyser(AnalysesEndpointAnalyser):
    def __init__(self, target_flag = TARGET_FLAG[2]):
        super().__init__(target_flag)

    def add_analysed_data_info(self, response):
        self.result_data.update({TARGET_NAME[self.target_flag]: response['meta']['url_info']['url']})

    def get_data_id(self):
        return requests.post(BaseAnalyser.API_URL + ENDPOINT[self.target_flag], headers={'x-apikey': self.api_key},
                             data={TARGET_NAME[self.target_flag]: self.data_for_analysis})
