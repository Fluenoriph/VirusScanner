# Файл 'base_report_generator.py': базовый класс для классов генераторов отчета от ресурса VirusTotal.

import abc
import os
from modules.real_time import CurrentTime


class BaseReportGenerator(abc.ABC):
    REPORT_FILE_TYPE = ('csv', 'json', 'html')

    def __init__(self, result_data, report_path): # If default path !
        self.result_data = result_data

        self.create_report_file = lambda file_type: os.path.join(report_path,
                                                    f'report_{CurrentTime.get_time().replace(':', '-')}.{file_type}')
                                                    # report type (name)
    @abc.abstractmethod
    def generate(self):
        pass
