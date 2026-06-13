import abc
from modules.data_validator.target_web_data_validator import TargetWebDataValidator
from modules.program_process.base_program_process import BaseProgramProcess
from modules.virus_analyser.direct_endpoint_analyser import DirectEndpointAnalyser


class ObjectVariantProgramProcess(abc.ABC, BaseProgramProcess):
    def __init__(self, cli_arguments):
        super().__init__(cli_arguments)

        self.target_data = self.validator.validate(cli_arguments[2])

        if self.target_data is False:
            print("Input data is invalid")
            #exit return code

        #analyser = DirectEndpointAnalyser(self.api_key, '/ip_addresses/', )

    @property
    @abc.abstractmethod
    def validator(self):
        pass

    @property
    @abc.abstractmethod
    def analyser(self):
        pass