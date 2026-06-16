# Файл 'json_report_generator.py': класс для формирования отчета в формате 'json'.

import json
from modules.report_generator.base_report_generator import BaseReportGenerator


class JsonReportGenerator(BaseReportGenerator):
    def __init__(self, result_data, report_path):
        super().__init__(result_data, report_path)

    def generate(self):
        with open(self.create_report_file(BaseReportGenerator.REPORT_FILE_TYPE[2]), "w", encoding="utf-8") as file:
            json.dump(self.result_data, file, indent=4)
            # test dump !!