import abc
from modules.virus_analyser.base_analyser import BaseAnalyser


class AnalysesEndpointAnalyser(BaseAnalyser, abc.ABC):
    def __init__(self, target_flag):
        super().__init__(target_flag)

    @abc.abstractmethod
    def get_data_id(self):
        pass

    def analyse(self):
        response_json_id = self.get_data_id()

        if response_json_id is not None:
            response_json_result = self.get_standard_request('/analyses/' + response_json_id['data']['id'])

            if response_json_result is not None:
                if self.check_bad_status_values(response_json_result):
                    self.add_current_time()
                    self.add_analysed_data_info(response_json_result)
                    self.add_stats(response_json_result)

                    return True

                else:
                    return False

            else:
                return False

        else:
            return False
