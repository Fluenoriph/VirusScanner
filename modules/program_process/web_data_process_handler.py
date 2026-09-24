from modules.program_process.base_program_process_handler import BaseProgramProcessHandler
from modules.app_data import TARGET_FLAG
from modules.virus_analyser.direct_endpoint_analyser import DirectEndpointAnalyser
from modules.virus_analyser.url_analyser import UrlAnalyser
from modules.data_validator.target_web_data_validator import TargetWebDataValidator


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

            result_payload = self.process_the_analysis(analyser)

            if result_payload is not False:
                print(result_payload)

                self.process_the_report(result_payload)
            else:
                print('Error connection to Virus Total')
                return

        else:
            print('BAD ARGUMENT')
            return
