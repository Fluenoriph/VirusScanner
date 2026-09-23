import abc
import time
from requests.exceptions import SSLError


class BaseProgramProcessHandler(abc.ABC):
    REQUEST_REPEAT_COUNT = 10
    DELAY_TO_AGAIN_REQUEST = 3

    # logger ???
    # input_data = ('virus_total_api_key', 'target_type', 'variant', 'data_to_analyse',
    # 'output', 'report_type', 'verbose')  no verbose !! (self.result)

    def __init__(self, api_key):
        self.api_key = api_key

    @abc.abstractmethod
    def process_the_object(self, data):
        pass

    @staticmethod
    def process_the_analysis(analyser_type):
        for _ in range(BaseProgramProcessHandler.REQUEST_REPEAT_COUNT):
            try:
                if analyser_type.analyse():

                    print("Result is OK !")  # logging ! Error code ?

                    return analyser_type.result_data
                else:
                    print("Result is NOT OK !")

                    time.sleep(BaseProgramProcessHandler.REQUEST_REPEAT_COUNT)

                    continue
            except SSLError:
                print('SSL Error')  # logging
                return False

        return False
