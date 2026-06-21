import abc
import os
from modules.program_process.process_code import ProcessCode as pc, ProcessCode


class BaseProgramProcessHandler(abc.ABC):
    # logger ???

    def __init__(self, input_data):
        #self.processing_code = 0

        self.api_key = input_data[0]
        self.target_data = input_data[1]  # ?? needed it ?

        self.check_target_data_parameter()

        if not os.path.exists(input_data[2]):
            os.makedirs(input_data[2])  # raise ??  test !
            self.output_path = input_data[2]

        self.report_format = input_data[3]
        self.target_type = input_data[4]


        self.virus_scanning()


        self.report_generating()

        if input_data[5]:
            pass
            # print console result  static class

    @abc.abstractmethod
    def check_target_data_parameter(self):
        pass

    @abc.abstractmethod
    def virus_scanning(self):
        pass

    @abc.abstractmethod
    def report_generating(self):
        pass