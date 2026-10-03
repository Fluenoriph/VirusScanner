"""
'direct_endpoint_analyser.py' - анализатор по принципу прямого запроса на эндпоинт.
По такому принципу анализируются IP адрес и доменное имя.
"""

from modules.virus_analyser.base_analyser import BaseAnalyser
from modules.app_data import ENDPOINT, TARGET_NAME


class DirectEndpointAnalyser(BaseAnalyser):
    def __init__(self, target_flag):
        super().__init__(target_flag)

    def analyse(self):
        response_json = self.get_standard_request(ENDPOINT[self.target_flag] + self.data_for_analysis)

        if response_json is not None:
            if self.check_null_status_values(response_json):
                self.add_current_time()
                self.add_analysed_data_info(response_json)
                self.add_stats(response_json)

                return True

            else:
                return False

        else:
            return False

    def add_analysed_data_info(self, response):
        self.result_data.update({ TARGET_NAME[self.target_flag]: response['data']['id'] })
