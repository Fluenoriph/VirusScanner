# 'base_report_generator.py' - базовый класс для классов генераторов отчета.

from abc import ABC, abstractmethod
import os
from pathlib import Path
from modules.real_time import get_current_time
from modules.app_data import TARGET_NAME, TARGET_FLAG


class BaseReportGenerator(ABC):
    def __init__(self, result_data, report_path, target_flag):
        self.result_data = result_data
        self.report_path = report_path
        self.target_flag = target_flag
        self.target_object = self.result_data[TARGET_NAME[self.target_flag]]
        self._report_file = None

    @property
    def report_file(self):
        return self._report_file

    @report_file.setter
    def report_file(self, value):
        self._report_file = value

    @abstractmethod
    def generate(self):
        pass

    def create_report_file(self, file_type):
        if self.target_flag is TARGET_FLAG[2]:
            x = self.target_object.replace('/', '-')
            self.target_object = x.replace(':', '-')

        return os.path.join(self.report_path, f'{self.target_object}-report_'
                            f'{get_current_time().replace(':', '-')}.{file_type}')
