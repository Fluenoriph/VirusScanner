# Файл 'program_process.py': класс для основного хода программы.
# 1. Парсинг лога сервера.
# 2. Проверка на VirusTotal.
# 3. Формирование и запись отчета.

from modules.log_parser import LogParser
from modules.virus_total_checker import VirusTotalChecker
from modules.csv_report_generator import CsvReportGenerator
from modules.json_report_generator import JsonReportGenerator
from modules.program_logger import ProgramLogger


class ProgramProcess:
    def __init__(self, source_log_file, api_key, result_log_path, result_log_format):
        logger = ProgramLogger()

        logger.logger.info('Program started')

        source_log_parser = LogParser(source_log_file)
        source_log_parser.parse()

        virus_analyzer = VirusTotalChecker(api_key, source_log_parser.matched_data, logger.logger)
        self._result = virus_analyzer.checks_result

        if result_log_format == 'csv':
            csv_report = CsvReportGenerator(self.result, result_log_path)
            csv_report.generate()

            logger.logger.info('CSV report generated')

        elif result_log_format == 'json':
            json_report = JsonReportGenerator(self.result, result_log_path)
            json_report.generate()

            logger.logger.info('JSON report generated')

    # Результат проверки в виде списка словарей. Используем для веб-интерфейса. Может нужен рефакторинг этого класса.

    @property
    def result(self):
        return self._result
