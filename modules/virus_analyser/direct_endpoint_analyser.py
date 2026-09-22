import time
from modules.virus_analyser.base_analyser import BaseAnalyser
from modules.app_data import ENDPOINT, TARGET_NAME


class DirectEndpointAnalyser(BaseAnalyser):
    def __init__(self, target_flag):
        super().__init__(target_flag)

    def analyse(self):
        for _ in range(BaseAnalyser.REQUEST_REPEAT_COUNT):
            response = self.standard_request_get(ENDPOINT[self.target_flag] + self.data_for_analysis)
            response_json = response.json()

            if self.check_bad_status_values(response_json):
                if response.status_code == BaseAnalyser.SUCCESSFUL_CODE:
                    self.add_time()
                    self.add_analysed_data_info(response_json)
                    self.add_stats(response_json)

                    return True
                else:
                    self.result_data.update(response_json)

                    return False

            else:
                time.sleep(BaseAnalyser.REQUEST_REPEAT_COUNT)

                continue

        return False

    def add_analysed_data_info(self, response):
        self.result_data.update({TARGET_NAME[self.target_flag]: response['data']['id']})
