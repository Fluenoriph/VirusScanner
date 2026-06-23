from modules.virus_analyser.base_analyser import BaseAnalyser
from modules.app_data import AppData


class DirectEndpointAnalyser(BaseAnalyser):
    def __init__(self, target_type):
        super().__init__(target_type)

    def analyse(self):
        response = self.standard_request_get(AppData.ENDPOINT[self.target_type] + self.data_for_analysis)
        response_json = response.json()

        if response.status_code == BaseAnalyser.SUCCESSFUL_CODE:
            self.add_time()
            self.add_analysed_data_info(response_json)
            self.add_stats(response_json)

            return True
        else:
            self.result_data.update(response_json)

            return False

    def add_analysed_data_info(self, response_json):
        self.result_data.update({self.target_type: response_json['data']['id']})
