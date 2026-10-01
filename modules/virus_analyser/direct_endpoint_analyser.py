from modules.virus_analyser.base_analyser import BaseAnalyser
from modules.app_data import ENDPOINT, TARGET_NAME


class DirectEndpointAnalyser(BaseAnalyser):
    def __init__(self, target_flag):
        super().__init__(target_flag)

    def analyse(self):
        response = self.get_standard_request(ENDPOINT[self.target_flag] + self.data_for_analysis)

        if response is not None:
            if self.check_bad_status_values(response):
                self.add_time()
                self.add_analysed_data_info(response)
                self.add_stats(response)

                return True

            else:
                return False

        else:
            return False

    def add_analysed_data_info(self, response):
        self.result_data.update({ TARGET_NAME[self.target_flag]: response['data']['id'] })
