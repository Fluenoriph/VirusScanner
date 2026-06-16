# Файл 'csv_report_generator.py': класс для формирования отчета в формате 'csv'.

import csv
from modules.report_generator.base_report_generator import BaseReportGenerator


class CsvReportGenerator(BaseReportGenerator):
    def __init__(self, result_data, report_path):
        super().__init__(result_data, report_path)
        self.columns = []

        if type(self.result_data) == dict:
            [self.columns.append(key) for key in self.result_data.keys()]
            self.write_csv = lambda writer: writer.writerow(self.result_data)
        else:
            [self.columns.append(key) for key in self.result_data[0].keys()]
            self.write_csv = lambda writer: writer.writerows(self.result_data)

    def generate(self):
        with open(self.create_report_file(BaseReportGenerator.REPORT_FILE_TYPE[1]), 'w', newline='',
                  encoding='utf-8') as file:

            writer = csv.DictWriter(file, fieldnames=self.columns)
            writer.writeheader()

            self.write_csv(writer)