from modules.app_data import TARGET, VARIANT
from modules.data_validator.target_web_data_validator import TargetWebDataValidator
from modules.virus_analyser.direct_endpoint_analyser import DirectEndpointAnalyser
from modules.virus_analyser.file_analyser_selector import FileAnalyserSelector
from modules.virus_analyser.url_analyser import UrlAnalyser


class ProgramProcessHandler:
    WEB_DATA_ANALYSER = {
        TARGET[0]: DirectEndpointAnalyser(TARGET[0]),
        TARGET[1]: DirectEndpointAnalyser(TARGET[1]),
        TARGET[2]: UrlAnalyser()
    }

    # logger ???

    # input_data = ('virus_total_api_key', 'data_to_analyse', 'target_type',
    # 'variant', 'output', 'report_type', 'verbose')  no verbose !! (self.result)

    def __init__(self, input_data):
        # target not file
        if input_data[2] is not TARGET[3]:
            if input_data[3] is VARIANT[0]:
                # object
                validator = TargetWebDataValidator(input_data[2])

                if validator.validate(input_data[1]):
                    analyser = ProgramProcessHandler.WEB_DATA_ANALYSER[input_data[2]]
                    analyser.api_key = input_data[0]
                    analyser.data_for_analysis = input_data[1]

                    if analyser.analyse():  # function ???
                        print("Result is OK !")
                    else:
                        print("Result is NOT OK !")
                    print(analyser.result_data)

                else:
                    print("Error") # BAD ARGUMENT !
            elif input_data[3] is VARIANT[1]:
                pass # log variant
            else:
                pass # dir variant


        # target is file
        else:
            file_size_selector = FileAnalyserSelector()

            if file_size_selector.select(input_data[1]):
                analyser = file_size_selector.result
                analyser.api_key = input_data[0]

                if analyser.analyse():   # duplicating !!
                    print("Result is OK !")
                else:
                    print("Result is NOT OK !")
                print(analyser.result_data)

            else:
                print(f"Error -- {file_size_selector.result}") # BAD ARGUMENT !
                # write to program log !!


    # method ?
    '''if not os.path.exists(input_data[4]):
            os.makedirs(input_data[4])  # raise ??  test !
            self.output_path = input_data[2]'''
