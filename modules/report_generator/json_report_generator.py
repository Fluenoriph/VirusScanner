# 'json_report_generator.py' - класс для формирования отчета в формате JSON.

import json
from modules.report_generator.base_report_generator import BaseReportGenerator
from modules.app_data import REPORT_FILE_TYPE


class JsonReportGenerator(BaseReportGenerator):
    def __init__(self, result_data, report_path, target_flag):
        super().__init__(result_data, report_path, target_flag)
        self.report_file = self.create_report_file(REPORT_FILE_TYPE[2])

    def generate(self):
        with open(self.report_file, 'w', encoding='utf-8') as file:
            json.dump(self.result_data, file, ensure_ascii=False, indent=4)
