# 'base_program_process_handler.py' - базовый класс для обработчиков логики программы.

from abc import ABC, abstractmethod
import time

from pygments.lexers import data
from requests.exceptions import SSLError
from modules.app_data import REPORT_FILE_TYPE, REQUEST_REPEAT_COUNT, DELAY_TO_AGAIN_REQUEST
from modules.report_generator.csv_report_generator import CsvReportGenerator
from modules.report_generator.html_report_generator import HtmlReportGenerator
from modules.report_generator.json_report_generator import JsonReportGenerator
from modules.program_logger import logging
from modules.program_codes import CODE_23, CODE_12


class BaseProgramProcessHandler(ABC):
    def __init__(self, api_key, target_flag, output_path, report_file_type):
        self.api_key = api_key
        self.target_flag = target_flag
        self._output_path = output_path
        self.report_file_type = report_file_type
        self.report_file = None

    @property
    def output_path(self):
        return self._output_path

    @output_path.setter
    def output_path(self, value):
        self._output_path = value

    @abstractmethod
    def process_the_object(self, data):
        pass

    @staticmethod
    def process_the_analysis(analyser_type):
        for _ in range(REQUEST_REPEAT_COUNT):
            try:
                process_result = analyser_type.analyse()

                if process_result:
                    return analyser_type.result_data
                elif process_result is None:
                    time.sleep(DELAY_TO_AGAIN_REQUEST)

                    continue
                else:
                    return None

            except SSLError:
                logging.error(CODE_23)

        return None

    def process_the_report(self, result_payload):
        if self.report_file_type is REPORT_FILE_TYPE[0]:
            report = HtmlReportGenerator(result_payload, self.output_path, self.target_flag)
            report.generate()

            self.report_file = report.report_file
            logging.info(f'{self.report_file_type.upper()} {CODE_12} - [{self.report_file}]')

        elif self.report_file_type is REPORT_FILE_TYPE[1]:
            report = CsvReportGenerator(result_payload, self.output_path, self.target_flag)
            report.generate()

            self.report_file = report.report_file
            logging.info(f'{self.report_file_type.upper()} {CODE_12} - [{self.report_file}]')

        elif self.report_file_type is REPORT_FILE_TYPE[2]:
            report = JsonReportGenerator(result_payload, self.output_path, self.target_flag)
            report.generate()

            self.report_file = report.report_file
            logging.info(f'{self.report_file_type.upper()} {CODE_12} - [{self.report_file}]')
