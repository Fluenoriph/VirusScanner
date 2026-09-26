import abc
import time
from pathlib import Path
from requests.exceptions import SSLError
from modules.app_data import REPORT_FILE_TYPE
from modules.report_generator.csv_report_generator import CsvReportGenerator
from modules.report_generator.html_report_generator import HtmlReportGenerator
from modules.report_generator.json_report_generator import JsonReportGenerator


class BaseProgramProcessHandler(abc.ABC):
    REQUEST_REPEAT_COUNT = 10
    DELAY_TO_AGAIN_REQUEST = 3

    def __init__(self, api_key, target_flag, output_path, report_file_type):
        self.api_key = api_key
        self.target_flag = target_flag
        self._output_path = output_path
        Path.mkdir(self.output_path, exist_ok=True)
        self.report_file_type = report_file_type

    @property
    def output_path(self):
        return self._output_path

    @output_path.setter
    def output_path(self, value):
        self._output_path = value

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

    def process_the_report(self, data):
        if self.report_file_type is REPORT_FILE_TYPE[0]:
            report = HtmlReportGenerator(data, self.output_path, self.target_flag)
            report.generate()
        elif self.report_file_type is REPORT_FILE_TYPE[1]:
            report = CsvReportGenerator(data, self.output_path, self.target_flag)
            report.generate()
        elif self.report_file_type is REPORT_FILE_TYPE[2]:
            report = JsonReportGenerator(data, self.output_path, self.target_flag)
            report.generate()
