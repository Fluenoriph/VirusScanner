import os

from modules.app_data import AppData
from modules.data_validator.target_web_data_validator import TargetWebDataValidator
from modules.program_process.process_code import ProcessCode as pc, ProcessCode


class ProgramProcessHandler:
    # logger ???

    # input_data = ('virus_total_api_key', 'data_to_analyse', 'target_type',
    # 'variant', 'output', 'report_type', 'verbose')

    def __init__(self, input_data):
        # target not file
        if input_data[2] is not AppData.TARGET[3]:
            if input_data[3] is AppData.VARIANT[0]:
                # object
                validator = TargetWebDataValidator(input_data[2])

                if validator.validate(input_data[1]):
                    analyser = AppData.WEB_DATA_ANALYSER[input_data[2]]
                    analyser.api_key = input_data[0]
                    analyser.data_for_analysis = input_data[1]
                else:
                    print("Error")

                    if analyser.analyse():
                        print("Result is OK !")
                    else:
                        print("Result is NOT OK !")

                    print(analyser.result_data)







    # method ?
    '''if not os.path.exists(input_data[4]):
            os.makedirs(input_data[4])  # raise ??  test !
            self.output_path = input_data[2]'''









        if input_data[5]:
            pass
            # print console result  static class
