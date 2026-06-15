from modules.data_validator.target_web_data_validator import TargetWebDataValidator
from modules.program_process.object_variant_program_process import ObjectVariantProgramProcess
from modules.data_validator.rgx_patterns import IP_ADDRESS
from modules.virus_analyser.direct_endpoint_analyser import DirectEndpointAnalyser


class IpObjectProcess(ObjectVariantProgramProcess):
    def __init__(self, input_data):
        super().__init__(input_data)

    @staticmethod
    def validator():
        return TargetWebDataValidator(IP_ADDRESS)

    def analyser(self):
        return DirectEndpointAnalyser(self.api_key, '/ip_addresses/', self.target_data, 'IP address')
