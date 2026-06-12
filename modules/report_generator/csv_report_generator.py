# Файл 'csv_report_generator.py': класс для формирования отчета в формате 'csv'.

import csv
from modules.report_generator.base_report_generator import BaseReportGenerator


class CsvReportGenerator(BaseReportGenerator):
    def __init__(self, result_data, report_path):
        super().__init__(result_data, report_path)

    def generate(self):
        with open(self.create_report_file(BaseReportGenerator.REPORT_FILE_TYPE[0]), 'w', newline='', encoding='utf-8') as file:
            columns = []
            [columns.append(key) for key in self.result_data[0].keys()]

            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()

            # Так как исходные данные - это список словарей, то проверим их количество для корректной записи.

            if len(self.result_data) > 1:
                writer.writerows(self.result_data)
            else:
                writer.writerow(self.result_data[0])
