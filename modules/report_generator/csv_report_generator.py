# 'csv_report_generator.py' - класс для формирования отчета в формате CSV.

import csv
from modules.app_data import REPORT_FILE_TYPE
from modules.report_generator.base_report_generator import BaseReportGenerator


class CsvReportGenerator(BaseReportGenerator):
    def __init__(self, result_data, report_path, target_flag):
        super().__init__(result_data, report_path, target_flag)
        self.report_file = self.create_report_file(REPORT_FILE_TYPE[1])

    def generate(self):
        with open(self.report_file, 'w', newline='', encoding='utf-8') as file:

            writer = csv.writer(file)
            writer.writerow(self.result_data.keys())
            writer.writerow(self.result_data.values())
