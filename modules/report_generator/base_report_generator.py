# 'base_report_generator.py' - базовый класс для классов генераторов отчета.

from abc import ABC, abstractmethod
import os
from pathlib import Path
from modules.real_time import get_current_time
from modules.app_data import TARGET_NAME


class BaseReportGenerator(ABC):
    def __init__(self, result_data, report_path, target_flag):
        self.result_data = result_data
        self.report_path = Path(report_path)
        self.report_path.mkdir(parents=True, exist_ok=True)
        self.target_object = self.result_data[TARGET_NAME[target_flag]]
        self._report_file = None

        self.create_report_file = lambda file_type: os.path.join(self.report_path,
                                                    f'{self.target_object}-report_'
                                                    f'{get_current_time().replace(':', '-')}.{file_type}')

    @property
    def report_file(self):
        return self._report_file

    @report_file.setter
    def report_file(self, value):
        self._report_file = value

    @abstractmethod
    def generate(self):
        pass
