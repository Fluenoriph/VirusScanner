"""
'analyses_endpoint_analyser.py' - базовый класс для анализаторов URL адреса и файлов менее 32 Мб.
Принцип реализован на отправке целевых данных через POST запрос с получением дескриптора (ID) объекта,
который потом используется для получения результатов анализа.
"""

from abc import ABC, abstractmethod
from modules.virus_analyser.base_analyser import BaseAnalyser


class AnalysesEndpointAnalyser(BaseAnalyser, ABC):
    def __init__(self, target_flag):
        super().__init__(target_flag)

    @abstractmethod
    def get_analysed_data_id(self):
        pass

    def analyse(self):
        response_json_data_id = self.get_analysed_data_id()

        if response_json_data_id is not None:
            response_json_result = self.get_standard_request('/analyses/' + response_json_data_id['data']['id'])

            if response_json_result is not None:
                if self.check_null_status_values(response_json_result):
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
