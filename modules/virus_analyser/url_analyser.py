import requests
from modules.app_data import TARGET, ENDPOINT
from modules.virus_analyser.analyses_endpoint_analyser import AnalysesEndpointAnalyser
from modules.virus_analyser.base_analyser import BaseAnalyser


class UrlAnalyser(AnalysesEndpointAnalyser):
    def __init__(self, target_type = TARGET[2]):
        super().__init__(target_type)

    def add_analysed_data_info(self, response):
        self.result_data.update( {self.target_type: response['meta']['url_info']['url']} )

    def get_data_id(self):
        return requests.post(BaseAnalyser.API_URL + ENDPOINT[self.target_type], headers={ 'x-apikey': self.api_key },
                             data={ self.target_type: self.data_for_analysis} )
