import abc
from modules.virus_analyser.base_analyser import BaseAnalyser


class AnalysesEndpointAnalyser(BaseAnalyser, abc.ABC):
    def __init__(self, target_type):
        super().__init__(target_type)

    @abc.abstractmethod
    def get_data_id(self):
        pass

    def analyse(self):
        response_id = self.get_data_id()
        response_id_json = response_id.json()

        if response_id.status_code == BaseAnalyser.SUCCESSFUL_CODE:
            response_result = self.standard_request_get('/analyses/' + response_id_json['data']['id'])
            response_result_json = response_result.json()

            if response_result.status_code == BaseAnalyser.SUCCESSFUL_CODE:
                self.add_time()
                self.add_analysed_data_info(response_result_json)
                self.add_stats(response_result_json)

                return True
            else:
                self.result_data.update(response_result_json)

                return False

        else:
            self.result_data.update(response_id_json)

            return False
