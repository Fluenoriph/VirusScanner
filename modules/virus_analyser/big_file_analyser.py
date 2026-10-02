import requests
from modules.app_data import TARGET_FLAG, ENDPOINT, TARGET_NAME
from modules.virus_analyser.base_analyser import BaseAnalyser
from modules.program_codes import CODE_200, CODE_27, CODE_409
from modules.program_logger import logger


class BigFileAnalyser(BaseAnalyser):
    def __init__(self, target_flag = TARGET_FLAG[3]):
        super().__init__(target_flag)

    def add_analysed_data_info(self, response):
        self.result_data.update({'md5': response['meta']['file_info']['md5']})
        self.result_data.update({'size': response['meta']['file_info']['size']})

    def analyse(self):
        response_json_upload_url = self.get_standard_request(ENDPOINT[self.target_flag][1])

        if response_json_upload_url is not None:
            with open(self.data_for_analysis, 'rb') as file:
                files = {TARGET_NAME[self.target_flag]: (self.data_for_analysis, file)}

                response_result_url = requests.post(response_json_upload_url['data'],
                                                    headers={ 'x-apikey': self.api_key }, files=files)

            if response_result_url.status_code == CODE_200:
                response_analysis_result = requests.get(response_result_url.json()['data']['links']['self'],
                                                        headers={ 'x-apikey': self.api_key })

                if response_analysis_result.status_code == CODE_200:
                    result_json = response_analysis_result.json()

                    if self.check_bad_status_values(result_json):
                        self.add_current_time()
                        self.add_analysed_data_info(result_json)
                        self.add_stats(result_json)

                        return True

                    else:
                        return False

                else:
                    return False

            elif response_result_url.status_code == CODE_409:
                logger.logger.warning(CODE_27)

                return False

            else:
                return False

        else:
            return False
