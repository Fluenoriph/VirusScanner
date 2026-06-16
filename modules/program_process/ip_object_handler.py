from modules.data_validator.target_web_data_validator import TargetWebDataValidator
from modules.data_validator.rgx_patterns import IP_ADDRESS
from modules.program_process.base_program_process_handler import BaseProgramProcessHandler
from modules.virus_analyser.direct_endpoint_analyser import DirectEndpointAnalyser


class IpObjectHandler(BaseProgramProcessHandler):
    def __init__(self, input_data):
        super().__init__(input_data)

    def check_target_data_parameter(self):
        validator = TargetWebDataValidator(IP_ADDRESS)

        if not validator.validate(self.target_data):
            pass
        # log error
        # exit 1

    def virus_scanning(self):
        scanner = DirectEndpointAnalyser(self.api_key, '/ip_addresses/', self.target_data, 'ip')