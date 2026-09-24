# Файл 'base_report_generator.py': базовый класс для классов генераторов отчета от ресурса VirusTotal.

import abc
import os
from pathlib import Path
from modules.app_data import TARGET_NAME
from modules.real_time import CurrentTime


class BaseReportGenerator(abc.ABC):
    def __init__(self, result_data, report_path, target_flag):
        self.result_data = result_data
        self.report_path = Path(report_path)
        self.report_path.mkdir(parents=True, exist_ok=True)
        self.target_object = self.result_data[TARGET_NAME[target_flag]]

        self.create_report_file = lambda file_type: os.path.join(self.report_path,
                                                    f'{self.target_object}-report_'
                                                    f'{CurrentTime.get_current_time().replace(':', '-')}.{file_type}')

    @abc.abstractmethod
    def generate(self):
        pass
