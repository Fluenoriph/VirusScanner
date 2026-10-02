from rich import print
from modules.program_process.base_program_process_handler import BaseProgramProcessHandler
from modules.app_data import TARGET_FLAG, SUCCESS_COLOR, FAILURE_COLOR, INFO_COLOR
from modules.virus_analyser.direct_endpoint_analyser import DirectEndpointAnalyser
from modules.virus_analyser.url_analyser import UrlAnalyser
from modules.data_validator.target_web_data_validator import TargetWebDataValidator
from modules.program_logger import logger
from modules.program_codes import CODE_21, CODE_24, CODE_11, CODE_13, CODE_14, CODE_10


class WebDataProcessHandler(BaseProgramProcessHandler):
    WEB_DATA_ANALYSER = {
        TARGET_FLAG[0]: DirectEndpointAnalyser(TARGET_FLAG[0]),
        TARGET_FLAG[1]: DirectEndpointAnalyser(TARGET_FLAG[1]),
        TARGET_FLAG[2]: UrlAnalyser()
    }

    def __init__(self, api_key, target_flag, output_path, report_file_type):
        super().__init__(api_key, target_flag, output_path, report_file_type)

    def process_the_object(self, data):
        validator = TargetWebDataValidator(self.target_flag)

        if validator.validate(data):
            analyser = WebDataProcessHandler.WEB_DATA_ANALYSER[self.target_flag]
            analyser.api_key = self.api_key
            analyser.data_for_analysis = data

            logger.logger.info(f'{CODE_10}--[{data}]')
            result_payload = self.process_the_analysis(analyser)

            if result_payload is not None:
                logger.logger.info(f'{CODE_11}--[{data}]')
                print(f'\n[{SUCCESS_COLOR}]> {CODE_11} ![/{SUCCESS_COLOR}]')

                self.process_the_report(result_payload)

                logger.logger.info(CODE_13)
                print(f'\n[{INFO_COLOR}]> {CODE_14} ![/{INFO_COLOR}]')

            else:
                logger.logger.critical(CODE_21)
                print(f'\n[{FAILURE_COLOR}]> {CODE_21} ![/{FAILURE_COLOR}]')

                return

        else:
            logger.logger.error(f'{CODE_24}--[{data}]')
            print(f'\n[{FAILURE_COLOR}]> {CODE_24} ![/{FAILURE_COLOR}]')

            return
