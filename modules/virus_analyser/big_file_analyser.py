import requests
from modules.app_data import TARGET, ENDPOINT
from modules.virus_analyser.base_analyser import BaseAnalyser


class BigFileAnalyser(BaseAnalyser):
    def __init__(self, target_type = TARGET[3]):
        super().__init__(target_type)

    def add_analysed_data_info(self, response_json):   # file class duplicate
        self.result_data.update({'md5': response_json['meta']['file_info']['md5']})
        self.result_data.update({'size': response_json['meta']['file_info']['size']})

    def analyse(self):
        response_upload_url = self.standard_request_get(ENDPOINT[self.target_type][1])
        response_upload_url_json = response_upload_url.json()

        if response_upload_url.status_code == BaseAnalyser.SUCCESSFUL_CODE:
            with open(self.data_for_analysis, 'rb') as file:
                files = { self.target_type: (self.data_for_analysis, file) }
                response_result_url = requests.post(response_upload_url_json['data'], headers=self.headers, files=files)
            response_result_url_json = response_result_url.json()

            if response_result_url.status_code == BaseAnalyser.SUCCESSFUL_CODE:   # maybe code 409
                response_analysis_result = requests.get(response_result_url_json['data']['links']['self'],
                                                        headers=self.headers)
                response_analysis_result_json = response_analysis_result.json()

                if response_analysis_result.status_code == BaseAnalyser.SUCCESSFUL_CODE:
                    self.add_time()
                    self.add_analysed_data_info(response_analysis_result_json)
                    self.add_stats(response_analysis_result_json)

                    return True
                else:
                    self.result_data.update(response_analysis_result_json)
                    print('Error 1')

                    return False

            elif response_result_url.status_code == 409:
                print('Link (big file) exist in Virus Total Base')

                return False
            else:
                self.result_data.update(response_result_url_json)
                print('Error 2')

                return False
        else:
            self.result_data.update(response_upload_url_json)
            print('Error 3')

            return False
