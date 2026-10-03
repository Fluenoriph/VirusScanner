# 'file_process_handler.py' - обработчик логики программы если анализируемый объект это файл.

from rich import print
from modules.target_data_validator.file_validator import FileValidator
from modules.program_process.base_program_process_handler import BaseProgramProcessHandler
from modules.virus_analyser.file_analyser_selector import FileAnalyserSelector
from modules.program_logger import logging
from modules.program_codes import CODE_21, CODE_11, CODE_26, CODE_25, CODE_13, CODE_14, CODE_10
from modules.app_data import SUCCESS_COLOR, FAILURE_COLOR, WARNING_COLOR, INFO_COLOR, DATA_COLOR, TARGET_NAME


class FileProcessHandler(BaseProgramProcessHandler):
    def __init__(self, api_key, target_flag, output_path, report_file_type):
        super().__init__(api_key, target_flag, output_path, report_file_type)

    def process_the_object(self, data):
        validator = FileValidator()

        if validator.validate(data):
            file_size_selector = FileAnalyserSelector()

            if file_size_selector.select(data):
                file_analyser = file_size_selector.analyser
                file_analyser.api_key = self.api_key

                logging.info(f'{CODE_10} - [{data}]')
                result_payload = self.process_the_analysis(file_analyser)

                if result_payload is not None:
                    logging.info(CODE_11)

                    print(f'\n[{DATA_COLOR}][ {result_payload[TARGET_NAME[self.target_flag]]} ][/{DATA_COLOR}] '
                          f'[{SUCCESS_COLOR}]> {CODE_11} ![/{SUCCESS_COLOR}]')

                    self.process_the_report(result_payload)

                    logging.info(CODE_13)
                    print(f'\n[{INFO_COLOR}]> {CODE_14} >[/{INFO_COLOR}] '
                          f'[{DATA_COLOR}][ {self.report_file} ][/{DATA_COLOR}]')

                else:
                    logging.critical(CODE_21)
                    print(f'\n[{FAILURE_COLOR}]> {CODE_21} ![/{FAILURE_COLOR}]')

                    return

            else:
                logging.warning(f'{CODE_26}--[{data}]')
                print(f'\n[{WARNING_COLOR}]> {CODE_26} ![/{WARNING_COLOR}]')

                return

        else:
            logging.error(CODE_25)
            print(f'\n[{FAILURE_COLOR}]> {CODE_25} ![/{FAILURE_COLOR}]')

            return
